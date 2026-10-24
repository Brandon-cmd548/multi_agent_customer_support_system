# NovaMart Multi-Agent Customer Support System

## Overview

NovaMart Multi-Agent Customer Support System is an enterprise-style AI customer support platform built on AWS as part of the AWS Future Agent Engineer program.

The project demonstrates how multiple specialized AI agents can collaborate to handle customer support requests, retrieve information from structured and unstructured data sources, apply business rules, and generate professional customer-facing responses.

## Key Features

### Multi-Agent Architecture

The system uses an Orchestrator → Workers pattern:

- **Orchestrator Agent** – Understands requests and routes work to specialists.
- **Inventory Agent** – Retrieves customer and order information from DynamoDB.
- **Policy Agent** – Uses Retrieval-Augmented Generation (RAG) across multiple Knowledge Bases.
- **Refund Agent** – Evaluates return eligibility based on customer tier and company policy.
- **Communication Agent** – Generates customer-friendly responses.

### Retrieval-Augmented Generation (RAG)

Policy questions are answered using multiple Amazon Bedrock Knowledge Bases:

- Returns Policy Knowledge Base
- Shipping Policy Knowledge Base
- Warranty Policy Knowledge Base

The Policy Agent performs parallel retrieval across all knowledge sources and combines the results into a grounded response.

### Enterprise Safety

Implemented with Amazon Bedrock Guardrails to:

- Filter harmful content
- Protect sensitive information (PII)
- Restrict off-topic discussions
- Apply enterprise safety policies consistently

### Memory & Context

AgentCore Memory provides:

- Session-aware conversations
- Multi-turn interactions
- Context retention across requests

### Cloud Observability

The solution includes:

- AWS CloudWatch logging
- AWS X-Ray tracing
- Service map visualization
- End-to-end request monitoring

## AWS Services Used

- Amazon Bedrock
- Amazon Bedrock AgentCore
- Amazon Bedrock Knowledge Bases
- Amazon Bedrock Guardrails
- Amazon DynamoDB
- Amazon S3
- AWS IAM
- AWS CloudFormation
- Amazon CloudWatch
- AWS X-Ray

## Technologies

- Python
- Strands Agents SDK
- Amazon Bedrock
- Retrieval-Augmented Generation (RAG)
- Multi-Agent Systems
- Agent Orchestration
- AI Safety & Governance

## Example Request Flow

```text
Customer Request
        │
        ▼
Orchestrator Agent
        │
 ┌──────┼──────────────────────┐
 │      │                      │
 ▼      ▼                      ▼
Inventory Agent        Policy Agent
 │                      │
 ▼                      ▼
DynamoDB           Knowledge Bases
                        │
                        ▼
                Returns / Shipping /
                    Warranty Data
        │
        ▼
Refund Agent
        │
        ▼
Communication Agent
        │
        ▼
Final Customer Response
```

## Skills Demonstrated

- AI Agent Development
- Multi-Agent Architecture
- Agent Orchestration
- Amazon Bedrock
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Cloud Solution Architecture
- DynamoDB Integration
- Knowledge Base Design
- Guardrail Implementation
- Cloud Observability
- Distributed Tracing
- Python Development

## Project Outcome

This project successfully demonstrates a production-style AI support workflow where multiple AWS-powered agents collaborate to:

- Understand customer intent
- Retrieve relevant business information
- Apply company rules and policies
- Make decisions
- Produce customer-ready communications
- Provide traceability and observability throughout the process

---

**Certification:** AWS Future Agent Engineer Program  
**Focus Areas:** Amazon Bedrock, Agentic AI, Multi-Agent Systems, RAG, Guardrails, Cloud-Native AI Solutions
