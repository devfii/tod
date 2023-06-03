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
