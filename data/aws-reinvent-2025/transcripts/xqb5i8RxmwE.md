---
video_id: xqb5i8RxmwE
video_url: https://www.youtube.com/watch?v=xqb5i8RxmwE
is_generated: False
is_translatable: True
summary: >-
  Eric Kessler, GM of Amazon Braket, and Michael Brett, head of Quantum Go-To-
  Market, explain AWS’s view of quantum computing as a future accelerator within
  the broader compute fabric, detail today’s capabilities of Amazon Braket, and
  showcase hybrid quantum-classical workflows including a drug-design case study
  with AstraZeneca, IonQ, NVIDIA, and AWS. They clarify that quantum computers are
  not faster classical machines but devices running fundamentally different
  algorithms that can provide exponential speedups for certain problems (e.g.,
  simulating quantum systems, factoring, optimization) yet remain slower and more
  expensive for many classical tasks. No current quantum computer solves industry-
  relevant problems faster, cheaper, or more accurately than classical alternatives,
  so today’s users are researchers studying devices, noise, and algorithms, closing
  the gap from bottom hardware to top applications. AWS pursues a four-pillar
  strategy: Amazon Braket (managed access to third-party QPUs and simulators),
  the Advanced Solutions Lab (professional services for quantum R&D), the AWS
  Center for Quantum Computing (hardware and error-correction research using
  cat-qubits with a 10x resource reduction for suppression demonstrated on the
  Ocelot chip), and post-quantum cryptography and networking teams. Braket provides
  on-demand or reserved access to ion-trap (IonQ, AQT), superconducting (Rigetti,
  IQM), and Rydberg (QuEra) devices plus circuit simulators, exposed through common
  interfaces compatible with Qiskit, PennyLane, NVIDIA CUDA-Q, and partner tools,
  with performance improvements such as Program Sets batching multiple circuits for
  up to 24x speedups by reducing compilation and I/O overhead. National initiatives
  and hubs (Singapore’s NQCH, UK’s NQCC, Ireland’s QCloud, Australia’s POSI) use
  Braket for democratized access, secure research environments, and administrative
  controls, accelerating scientific discovery in physics and chemistry where up to
  30–50% of supercomputing workloads could see exponential quantum benefits.
  Looking toward enterprise adoption, Brett outlines AWS’s Quantum Embark program
  (12-week fixed-scope discovery, training, and benchmarking), deeper ASL
  engagements generating proprietary algorithms and IP, and integration of Braket
  as another accelerator within AWS HPC services (Batch, ParallelCluster, Parallel
  Compute Service) so hybrid workloads orchestrate CPUs, GPUs, Trainium, and QPUs.
  He emphasizes starting now to build know-how and IP before quantum advantage
  arrives, citing JPMorgan Chase’s multi-year collaboration benchmarking quantum
  and classical approaches. The AstraZeneca case demonstrates end-to-end hybrid
  orchestration: a quantum routine on IonQ Forte-1 prepares trial wavefunctions for
  transition metal catalysis (oxidative addition in Suzuki-Miyaura coupling),
  feeding classical Monte Carlo post-processing on 40 P5eN (H100) instances via
  ParallelCluster. The hybrid workflow achieved a 656x speedup on that trial stage
  versus previous classical methods, hinting at future ability to model larger
  molecules like FeMoCo and inform synthesis routes, though not yet production-
  ready given cost and engineering tricks. Brett concludes with actions: generate
  quantum IP and workforce skills, engage suppliers across hardware/software,
  and leverage Braket (free badges, workshops, Embark, ASL, Braket Direct) to
  experiment now. A catalog of re:Invent sessions covers financial applications,
  hybrid compute, gen-AI-assisted quantum development, and hub implementations,
  underscoring AWS’s goal to make quantum “boring” by integrating it as a secure,
  scalable, policy-driven accelerator alongside existing AWS compute.
keywords: Amazon Braket, quantum computing, hybrid workflows, AstraZeneca case study, error correction
---
