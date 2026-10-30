# MCTQ Social Jetlag & Sleep Debt Chronobiology Pacer Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Munich ChronoType Questionnaire (MCTQ) mid-sleep on free days (MSFsc) correction, social jetlag calculation, and cumulative sleep debt recovery pacer. Built for GenPark (https://www.genpark.ai).

## Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## MCP Tools Exposed
- `calculate_mctq_corrected_mid_sleep`: Calculate sleep-corrected mid-sleep on free days (MSFsc) to classify true internal biological chronotype.
- `compute_social_jetlag_and_debt_recovery`: Compute social jetlag disparity (hours) between work and free days and synthesize sleep debt repayment schedule.

## Installation & Usage
```bash
python -m genpark_personal_agent_mctq_social_jetlag_sleep_debt_skill.server --test
```
