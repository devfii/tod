# tod

Creating a repository on ECR
1. install aws cli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

For detailed instructions on installing AWS CLI v2  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions

2. Configure AWS CLI
aws configure


3. Create repo
aws ecr create-repository \
    --repository-name tod

4. Create ecr repository policy
aws ecr put-lifecycle-policy \
    --repository-name "tod" \
    --lifecycle-policy-text "file://repository_policy.json"


aws ecs create-cluster \
--cluster-name   todCluster   --capacity-providers   FARGATE \
--default-capacity-provider-strategy capacityProvider=FARGATE,weight=1 


aws ecs register-task-definition \
    --cli-input-json file:task_definition.json


Github actions
Create secrets
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY

variables
AWS_REGION
ECR_REPOSITORY
