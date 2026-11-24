# R130 — CMOS Microprocessor Arithmetic Logic Unit (ALU)

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R130 · 8-BIT STORED-PROGRAM PROCESSOR & ALU              ║
║  End product: Operational CMOS Microprocessor (MOS 6502 class)   ║
║  Transistor count: 3,510 transistors, Clock frequency: 2 MHz     ║
╠══════════════════════════════════════════════════════════════════╣
║  BOOLEAN LOGIC TO GENERAL COMPUTATION                            ║
║    All mathematical and algorithmic computation reduces to three ║
║    primitives implemented in planar CMOS transistors [→ R101]:   ║
║    1. NOT Gate (CMOS Inverter: 1 PMOS pull-up + 1 NMOS pull-down)║
║    2. NAND Gate (2 PMOS parallel + 2 NMOS series)                ║
║    3. NOR Gate (2 PMOS series + 2 NMOS parallel)                 ║
║    NAND is functionally complete: ANY mathematical function,     ║
║    from simple addition to a neural network, can be synthesized  ║
║    purely from interconnected NAND gates!                        ║
╠══════════════════════════════════════════════════════════════════╣
║  CORE MICRO-ARCHITECTURE                                         ║
║                                                                  ║
║  1. 8-BIT ARITHMETIC LOGIC UNIT (ALU)                            ║
║     • Built from 8 cascaded 1-bit Full Adders:                   ║
║       Sum = A ⊕ B ⊕ Carry_in                                     ║
║       Carry_out = (A · B) + (Carry_in · (A ⊕ B))                 ║
║     • Performs: ADD, ADC, SUB, AND, ORA, EOR, ASL, ROL.          ║
║                                                                  ║
║  2. REGISTER FILE                                                ║
║     • Accumulator (A register): 8-bit dynamic latch.             ║
║     • Index Registers (X, Y): 8-bit counters.                    ║
║     • Program Counter (PC): 16-bit register (addresses 64 kB).   ║
║     • Stack Pointer (S) & Processor Status Register (Flags: N,Z).║
║                                                                  ║
║  3. INSTRUCTION DECODER & SEQUENCER (CONTROL UNIT)               ║
║     • PLA (Programmable Logic Array) matrix: decodes fetched     ║
║       8-bit opcodes (e.g., 0xA9 = LDA #immediate) into control   ║
║       enable lines for ALU registers across clock phases Φ1, Φ2. ║
║                                                                  ║
║  4. 64 KILOBYTE MEMORY BUS                                       ║
║     • 16 address lines (A0–A15) + 8 bidirectional data lines     ║
║       (D0–D7) + Read/Write (R/W) control.                        ║
╠══════════════════════════════════════════════════════════════════╣
║  BOOT CODE EXECUTION: Apply 5V power and release Reset line:     ║
║  Processor reads reset vector from address 0xFFFC-0xFFFD, loads  ║
║  program counter, and begins executing deterministic stored      ║
║  machine instructions at 2 million clock cycles per second!      ║
╚══════════════════════════════════════════════════════════════════╝
```
