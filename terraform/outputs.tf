output "public_ip" {
  description = "Public IP address of the LearnHub server"
  value       = aws_instance.learnhub.public_ip
}

output "jenkins_url" {
  description = "Jenkins dashboard URL"
  value       = "http://${aws_instance.learnhub.public_ip}:8080"
}

output "application_url" {
  description = "LearnHub application URL"
  value       = "http://${aws_instance.learnhub.public_ip}:5000"
}
