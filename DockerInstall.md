
# Installing and Running AutoTrain-Advanced in a Docker Container on Arch Linux

This guide will walk you through the steps to set up and run AutoTrain-Advanced in a Docker container on Arch Linux.

---

## Prerequisites

Ensure the following are installed and configured on your system:
- **Docker**: Follow the [official Docker installation guide](https://docs.docker.com/engine/install/archlinux/) if not already installed.
- **Git**: Use `sudo pacman -S git` to install it if missing.
- **NVIDIA GPU Drivers**: Ensure your GPU drivers and Docker NVIDIA toolkit are correctly installed for GPU support.

---

## Installation Steps

1. **Clone the AutoTrain-Advanced Repository**

   ```bash
   git clone git@github.com:cycloarcane/autotrain-advanced.git
   cd autotrain-advanced
   ```

2. **Start the Docker Service**

   ```bash
   sudo systemctl start docker
   ```

3. **Build the Docker Image**

   ```bash
   sudo docker build -t autotrain-advanced -f Dockerfile .
   ```

4. **Run the Docker Container**

   ```bash
   sudo docker run --gpus all -it --rm -p 8080:8080 autotrain-advanced
   ```

---

## Inside the Docker Container

After the container starts, perform the following steps:

1. **Initialize Conda**

   ```bash
   conda init
   source ~/.bashrc
   ```

2. **Activate the Environment**

   ```bash
   conda activate /app/env
   ```

3. **Start the AutoTrain Application**

   ```bash
   autotrain app --host 0.0.0.0 --port 8080 --workers 4
   ```

---

## Access the Application

Once the application is running, open your browser and navigate to:

```
http://127.0.0.1:8080
```

You should see the AutoTrain-Advanced interface.

---

## Notes

- Ensure that your GPU is properly configured to work with Docker if you encounter any issues.
- Adjust the port mapping (`-p 8080:8080`) if you want to use a different port.

---

Enjoy using AutoTrain-Advanced!
