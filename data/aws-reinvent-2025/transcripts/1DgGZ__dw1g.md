---
video_id: 1DgGZ__dw1g
video_url: https://www.youtube.com/watch?v=1DgGZ__dw1g
is_generated: False
is_translatable: True
summary: "In this session, Kohei \"Max\" Matsui, an AWS Hero and IoT/AI Evangelist at Soracom, introduces the concept of \"Physical AI\"—artificial intelligence that interacts with the physical world through sensors and actuators to perform tasks like robotic manipulation. Max begins by distinguishing Physical AI from standard cloud-based Generative AI, emphasizing that while cloud models operate on digital data, Physical AI must perceive and influence real-world environments. He argues that for applications such as industrial robotics, relying solely on cloud inference is often impractical due to latency constraints, safety requirements, and the need for offline autonomy. To illustrate this, Max conducts a compelling live demonstration comparing two robotic arms: one controlled locally via USB, which moves instantly, and another controlled via a cloud relay (LTE to US-East-1), which suffers from a noticeable 500-600 millisecond delay. He cites the \"100-millisecond barrier\" as a critical threshold; any latency beyond this is perceptible to humans and can be dangerous or inefficient in fast-paced production lines where objects move rapidly on conveyor belts.

The core technology enabling this shift is the **Vision-Language-Action (VLA)** model, a multimodal AI capable of processing visual input and text instructions to generate physical action plans, not just text or images. Max shares a customer use case from Linku, a Japanese company using 3D scanners and VLA models to allow robots to intelligently pick varied objects, adjusting to unpredictable orientations that would break traditional rule-based \"teaching\" methods. However, running these sophisticated VLA models at the edge introduces a significant challenge: **updatability**. Edge devices have fixed resources, and AI models evolve rapidly. A device deployed with today's state-of-the-art model will be obsolete within months if the model cannot be easily swapped or upgraded. Physical AI systems, therefore, must treat hardware like software, prioritizing continuous deployment pipelines over static firmware.

To solve the deployment challenge, Max details a robust architecture using **AWS IoT Greengrass V2**. He recommends packaging AI models directly into **Docker containers** and managing them as Greengrass components. This approach treats the heavy VLA model effectively as a microservice that can be orchestrated from the cloud. In a step-by-step technical walkthrough, he demonstrates updating a live robot's \"brain\" from a model trained to detect black boxes to one trained for white boxes. By building a new Docker image containing the updated model, pushing it to **Amazon Elastic Container Registry (ECR)**, and updating the Greengrass deployment, the edge device seamlessly pulls and applies the new capability without a complete firmware OTA. Max concludes by discussing strategies for handling the massive file sizes of GenAI models, advising that bundling models within the Docker container is generally the most reliable method for avoiding the 2GB artifact limit of Greengrass, provided one has adequate bandwidth via LTE or Wi-Fi."
keywords:
  - Physical AI
  - AWS IoT Greengrass
  - VLA Models
  - Edge Inference
  - Robotics
---
