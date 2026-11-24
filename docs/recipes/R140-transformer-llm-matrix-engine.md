# R140 — Transformer LLM Matrix Multiply-Accumulate Engine

```
╔══════════════════════════════════════════════════════════════════╗
║  RECIPE R140 · SYSTOLIC ARRAY TENSOR PROCESSOR FOR TRANSFORMERS  ║
║  End product: 128 × 128 BF16 Tensor Processing Matrix Core       ║
║  Compute throughput: 32 TeraFLOPS at 1.0 GHz clock               ║
╠══════════════════════════════════════════════════════════════════╣
║  HOW LARGE LANGUAGE MODELS ACTUALLY EXECUTE                      ║
║    At mathematical bottom, every modern LLM (GPT-4, Gemini)      ║
║    consists of repeated transformer blocks executing:            ║
║                                                                  ║
║    1. Multi-Head Scaled Dot-Product Attention:                   ║
║       Attention(Q, K, V) = softmax( (Q · K^T) / sqrt(d_k) ) · V  ║
║                                                                  ║
║    2. Feed-Forward SwiGLU / MLP Projections:                     ║
║       FFN(x) = (silu(x · W_gate) * (x · W_up)) · W_down          ║
║                                                                  ║
║    99.2% of ALL FLOPS in an LLM are General Matrix Multiplies    ║
║    (GEMM): C = A · B + C.                                        ║
║    Standard CPUs waste 90% of energy fetching instructions.      ║
║    A Systolic Array streams data through an interconnected grid  ║
║    of multiply-accumulators with zero memory bus overhead!       ║
╠══════════════════════════════════════════════════════════════════╣
║  HARDWARE IMPLEMENTATION (128 × 128 Systolic Array)              ║
║                                                                  ║
║  A) 16,384 Processing Elements (PEs) arranged in 2D grid:        ║
║     Each PE contains:                                            ║
║     • BF16 Multiplier (Bfloat16: 1 sign, 8 exponent, 7 mantissa) ║
║     • FP32 Accumulator register (preserves mathematical precision║
║       across 128 dot-product additions without overflow)         ║
║     • Horizontal data register (passes Matrix A elements right)  ║
║     • Vertical data register (passes Matrix B elements down)     ║
║                                                                  ║
║  B) High-Bandwidth On-Chip SRAM Cache (64 Megabytes):            ║
║     Pipelined memory banks supplying 4 Terabytes/sec bandwidth.  ║
╠══════════════════════════════════════════════════════════════════╣
║  DATA FLOW EXECUTION                                             ║
║    1. Weight matrix W (e.g. 4096 × 4096 attention weights) is    ║
║       loaded and pre-stationed inside PE accumulator registers.  ║
║    2. Activation vector X (token embeddings) enters from the left║
║       wavefront, staggered by 1 clock cycle per row.             ║
║    3. At every clock tick, each PE multiplies input by weight,   ║
║       adds to running sum, and passes data to right neighbor.    ║
║    4. Result matrix C exits right edge with 100% hardware duty   ║
║       cycle efficiency: enables generating tokens in real-time!  ║
╚══════════════════════════════════════════════════════════════════╝
```
