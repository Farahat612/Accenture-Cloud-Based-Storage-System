# AWS Cloud-Based Storage System Architecture Diagram

> This is a System Architecture Diagram that serves as first task of an AWS cloud-Based Storage System project for for Accenture company hosted by Qureos website.

> <p align="center">
>   <img width="100%" src="System Diagram.png">
> </p>

## Task outline

### Scenario:

Design a scalable and secure system architecture for a cloud-based storage service. The architecture should handle large amounts of data, ensure data security, and provide efficient access control mechanisms.

### Deliverable:

- Comprehensive system architecture diagram.
- Document explaining design decisions, scalability considerations, and security measures.

## Overview

This repository outlines the design decisions, scalability considerations, security measures, and additional features of the Cloud-Based Storage System Architecture.

## Design Decisions

### Cloud Service Provider (CSP)

The architecture leverages a reputable Cloud Service Provider, such as AWS, for its robust infrastructure, scalability features, and a comprehensive set of cloud services.

### Storage Components

1. **S3 Buckets**: Scalable and durable object storage for ease of use, scalability, and redundancy features.

2. **Glacier for Archival Storage**: Low-cost archival storage with data retrieval options, suitable for long-term data retention.

### Database / Data Storage

DynamoDB is employed as the database for storing metadata due to its NoSQL nature, allowing for flexible schema design and seamless scalability.

### API Gateway

API Gateway is employed for access control, rate limiting, and as a central entry point for managing API requests.

### Authentication Service

AWS Identity and Access Management (IAM) is chosen for authentication, providing fine-grained access controls and seamless integration with other AWS services.

### Encryption Service

AWS Key Management Service (KMS) is used for encryption, ensuring data confidentiality through secure and centralized key management.

### File Management APIs

Custom APIs for file upload, download, and sharing provide controlled access to the storage system.

### User Access Interface

A web interface serves as the user access point, providing a user-friendly experience for interacting with the cloud-based storage system.

## Scalability Considerations

### Storage Components

- **S3 Buckets**: Automatically scales storage capacity to accommodate increasing amounts of data.

- **DynamoDB**: Dynamically scales read and write capacity based on demand, facilitating scalability.

### API Gateway

API Gateway can handle a large number of concurrent requests, with scalability managed by AWS behind the scenes.

### Additional Scalability Components

- **CDN (Content Delivery Network)**: Enhances scalability by distributing content globally, reducing latency, and handling a large number of requests efficiently.

- **Load Balancer**: Distributes incoming network traffic across multiple servers to ensure optimal resource utilization and prevent overload on individual components.

- **Auto-Scaling Mechanism**: Automatically adjusts the number of compute resources based on demand, enhancing system scalability during traffic spikes.

## Security Measures

### Encryption Techniques

- **Data at Rest**: AES-256 encryption for data stored in S3 buckets and DynamoDB ensures the confidentiality and integrity of stored information.

- **Data in Transit**: Secure data transmission is guaranteed through the use of HTTPS, facilitated by the TLS protocol.

### Authentication and Access Control

- **AWS IAM**: Provides secure user authentication and access control to AWS resources, ensuring that only authorized users can interact with the cloud-based storage system.

### Additional Security Measures

- **AWS KMS**: Manages encryption keys, ensuring secure key storage and access control.

- **Redundancy & Failover Systems**: Inclusion of redundancy mechanisms enhances system robustness, minimizing the impact of potential failures.

## Conclusion

The Cloud-Based Storage System Architecture is designed to be scalable, secure, and robust. Leveraging industry-leading cloud services ensures optimal performance and reliability. The design decisions, scalability considerations, and security measures collectively contribute to the creation of a resilient and efficient cloud-based storage system.
