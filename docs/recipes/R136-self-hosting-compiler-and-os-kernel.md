# R136 — Self-Hosting Compiler & Preemptive Unix-like OS Kernel

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R136 · SELF-HOSTING C COMPILER & MULTITASKING OS KERNEL  ║
║  End product: 1 × POSIX-Compliant 32/64-Bit Operating System     ║
║  Capabilities: Preemptive scheduling, Virtual memory, ELF linking ║
╠══════════════════════════════════════════════════════════════════╣
║  PURPOSE IN RECURSIVE CHAIN                                      ║
║    The foundational software bootstrap prerequisite for:         ║
║    • Decoupling high-level software algorithms from physical raw ICs║
║    • Multi-user database systems and concurrent networking [→ R134]║
║    • Automated compilation of scientific simulations and CAD tools ║
╠══════════════════════════════════════════════════════════════════╣
║  RECURSIVE INGREDIENT & TOOL DEPENDENCIES                        ║
║    1. CMOS Microprocessor & ALU Target Hardware: 1 [→ R130]      ║
║    2. Volatile RAM & Non-Volatile Flash Boot ROM: 1 [→ R131, R132]║
║    3. Memory Management Unit (MMU) with Paging Hardware: 1       ║
║    4. Standard ASCII Serial UART Terminal Console: 1 [→ R130]    ║
║    5. Stage 0 Minimal Bootstrap Hex Machine Monitor: 1 [→ R130]  ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 1: COMPILER BOOTSTRAP CASCADE (STAGE 0 TO SELF-HOSTING)   ║
║    1a. Stage 0 (Hand-Assembled Hexadecimal Machine Code):        ║
║        Toggle 256 bytes of raw binary opcodes into ROM [→ R132]  ║
║        via front-panel switches to create a primitive Forth/hex  ║
║        monitor that reads ASCII characters from serial UART.     ║
║    1b. Stage 1 (Minimal Macro Assembler):                        ║
║        Write a 500-line assembler in Stage 0: Translates symbolic║
║        assembly mnemonics (`MOV`, `ADD`, `JMP`, `CALL`, `RET`)   ║
║        into binary machine words.                                ║
║    1c. Stage 2 (Subset C Compiler in Assembly):                  ║
║        Write a recursive-descent C compiler in assembly that     ║
║        supports basic types (`int`, `char`, `pointer`), control  ║
║        structures (`if`, `while`, `for`), and function calls.    ║
║    1d. Stage 3 (Full ANSI C Compiler written in Subset C):       ║
║        Write complete optimizing C compiler frontend & backend:  ║
║        • Lexer: Tokenizes source code into token stream.         ║
║        • Parser: Builds Abstract Syntax Tree (AST).              ║
║        • Intermediate Representation (IR) & Register Allocator:  ║
║          Applies Chaitin graph-coloring register allocation.     ║
║        • Code Generator: Emits native machine instructions.      ║
║    1e. The Self-Hosting Milestone: Compile the compiler with     ║
║        itself! The compiler can now compile any new version of   ║
║        itself and the entire operating system codebase.          ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 2: PREEMPTIVE UNIX-LIKE KERNEL ARCHITECTURE               ║
║    2a. Hardware Timer Interrupt: Configure 1,000 Hz programmable ║
║        hardware interval timer [→ R130]. Every 1.0 millisecond,  ║
║        timer fires an interrupt, preempting the CPU.             ║
║    2b. Round-Robin Process Scheduler: Saves CPU register context ║
║        onto current process stack; selects highest-priority      ║
║        runnable process; restores its registers; resumes thread. ║
║    2c. Virtual Memory & 4 KB Paging: Hardware MMU translates     ║
║        virtual addresses to physical DRAM [→ R131] via two-level ║
║        page tables:                                              ║
║        • Isolates every user process in its own 4 GB address space║
║        • Prevents a crashing application from corrupting the     ║
║          kernel or other processes!                              ║
║    2d. System Call Interface (Trap gate / Syscall opcode):       ║
║        User programs cross privilege boundary into Kernel Ring 0 ║
║        to request I/O (`fork`, `execve`, `read`, `write`, `open`,║
║        `close`, `mmap`, `socket`).                               ║
╠══════════════════════════════════════════════════════════════════╣
║  STAGE 3: VIRTUAL FILE SYSTEM & SHELL ENVIRONMENT                ║
║    3a. Unix Inode File System: Implements hierarchical directory ║
║        tree (`/`, `/bin`, `/dev`, `/etc`, `/home`); files are    ║
║        stored as arrays of indirect data blocks on disk [→ R132].║
║    3b. Everything is a file abstraction: Hardware devices        ║
║        (UART console, disks, network interfaces) are accessed as ║
║        byte streams in `/dev/`.                                  ║
║    3c. Command Shell & Standard C Library (libc):                ║
║        Compile interactive command interpreter (`sh`), core      ║
║        utilities (`ls`, `cp`, `cat`, `grep`, `vi`), and linkers. ║
╠══════════════════════════════════════════════════════════════════╣
║  QUALITY CONTROL METRICS                                         ║
║    • Self-hosting identity: Triple-stage compiler build produces ║
║      bit-for-bit identical binaries ($md5sum\text{ match}$).     ║
║    • Context switch latency: $<2.5\ \mu\text{s}$ per thread switch.║
║    • Kernel stability: $>1,000\text{ hours}$ uptime under stress.║
╚══════════════════════════════════════════════════════════════════╝
```
