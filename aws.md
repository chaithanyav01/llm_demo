aws account id
592573568306

aws configure list-profiles

aws configure --profile personal

aws sts get-caller-identity --profile personal --query Account --output text

aws ecr create-repository --repository-name tinygpt-api --region ap-south-1 --profile personal

aws ecr get-login-password --region ap-south-1 --profile personal | docker login --username AWS --password-stdin 592573568306.dkr.ecr.ap-south-1.amazonaws.com

docker tag tinygpt-api:latest 592573568306.dkr.ecr.ap-south-1.amazonaws.com/tinygpt-api:2026-02-27