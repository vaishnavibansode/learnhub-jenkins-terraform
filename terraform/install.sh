#!/bin/bash
set -e

apt-get update
apt-get install -y \
    openjdk-21-jre \
    python3 \
    python3-venv \
    python3-pip \
    curl \
    git

# Install Jenkins
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key \
    -o /usr/share/keyrings/jenkins-keyring.asc

echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/" \
    > /etc/apt/sources.list.d/jenkins.list

apt-get update
apt-get install -y jenkins

systemctl enable jenkins
systemctl start jenkins

# Allow Jenkins to manage the Flask service
usermod -aG sudo jenkins

echo "Jenkins installation completed."

# Allow Jenkins to execute deployment commands without a password
echo "jenkins ALL=(ALL) NOPASSWD:ALL" | tee /etc/sudoers.d/jenkins
chmod 440 /etc/sudoers.d/jenkins
visudo -cf /etc/sudoers.d/jenkins
