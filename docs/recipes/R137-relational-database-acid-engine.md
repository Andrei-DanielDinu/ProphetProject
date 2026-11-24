# R137 — Relational Database Management System (RDBMS & B-Tree ACID Engine)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R137 · RELATIONAL DATABASE (RDBMS ACID ENGINE)          ║
║  End product: 1 × High-Performance SQL Relational Database Server║
║  ACID guarantees: Atomicity, Consistency, Isolation, Durability  ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The structured data persistence and transaction engine for:   ║
║    • Banking and central clearinghouse balance ledgers [→ R401]  ║
║    • Land cadastre parcel ownership and demographic census [→ R403]║
║    • Manufacturing inventory MRP, supply chains, and hospital EHR║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. Unix-like Operating System Kernel & POSIX APIs: [→ R136]   ║
║    2. Dynamic RAM Buffer Pool Cache (16 GB): [→ R131]            ║
║    3. Non-Volatile Flash / Magnetic Disk Array: [→ R132]         ║
║    4. C99 Standard ANSI Compiler & Toolchain: 1 [→ R136]         ║
║    5. TCP/IP Socket Network Stack: 1 [→ R134]                    ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: STORAGE ENGINE & B+ TREE INDEXING                      ║
║    1a. Fixed 8 KB Page Buffer Pool: Storage files are partitioned║
║        into 8,192-byte slotted pages on disk. The Buffer Pool    ║
║        Manager caches pages in DRAM using LRU-2 replacement.     ║
║    1b. B+ Tree Index Architecture:                               ║
║        • Root and interior branch nodes contain search keys and  ║
║          child page pointers (fanout $>100$).                    ║
║        • Leaf nodes contain record pointers (Row IDs) and are    ║
║          doubly-linked horizontally for fast sequential scans.   ║
║        • Search, insert, and delete complexity: $O(\log N)$.     ║
║        • A 3-level B+ tree can index 1,000,000,000 rows with     ║
║          only 3 page lookups!                                    ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: ACID COMPLIANCE & WRITE-AHEAD LOGGING (WAL)            ║
║    2a. The ARIES Recovery Algorithm:                             ║
║        • Write-Ahead Logging (WAL): Before any database page is  ║
║          written to disk, the corresponding log record must be   ║
║          flushed to persistent storage (`fsync`)!                ║
║    2b. Atomicity & Durability: Every transaction records:        ║
║        $\text{Log Sequence Number (LSN)}$, $\text{Transaction ID}$,║
║        $\text{Page ID}$, $\text{Redo Data}$, $\text{Undo Data}$.  ║
║        If power is cut mid-transaction:                          ║
║        • Analysis Pass: Identifies dirty pages and active txns.  ║
║        • Redo Pass: Replays logged updates to restore state.     ║
║        • Undo Pass: Rolls back uncommitted transactions. Zero data║
║          loss or corruption!                                     ║
║    2c. Isolation & Multi-Version Concurrency Control (MVCC):     ║
║        Every record carries creation transaction ID ($xmin$) and ║
║        deletion transaction ID ($xmax$). Readers never block     ║
║        writers; writers never block readers!                     ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: SQL PARSER & COST-BASED OPTIMIZER                      ║
║    3a. Lexical analysis & parsing: Compiles declarative SQL:     ║
║        `SELECT name, balance FROM accounts WHERE balance > 1000` ║
║        into relational algebra tree ($\sigma, \pi, \bowtie$).    ║
║    3b. Cost-Based Query Optimizer (CBO): Estimates disk I/O and  ║
║        CPU cost across candidate execution plans using table     ║
║        column histograms: Chooses between Index Scan vs Seq Scan,║
║        and Nested Loop vs Hash Join vs Merge Join.               ║
║    3c. Volcano Iterator Execution: Nodes implement `open()`,     ║
║        `next()`, `close()` pipelined row processing.             ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Transaction throughput: $>50,000\text{ TPC-B TPS}$ sustained.║
║    • Crash recovery test: 100 sudden power-kill cycles during    ║
║      heavy write load; 0 corrupted rows, 100% balance integrity. ║
║    • Read latency: $<100\ \mu\text{s}$ point queries on index.   ║
╚══════════════════════════════════════════════════════════════════╝
```
