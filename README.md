# tod

##aws 
1. install aws cli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

For detailed instructions on installing AWS CLI v2  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions

2. Configure AWS CLI
aws configure

3. Create VPC and networking resources
aws cloudformation create-stack --stack-name todstack --template-body file://aws/resources.yaml
aws cloudformation create-stack --stack-name repostack --template-body file://aws/containers.yaml --capabilities CAPABILITY_NAMED_IAM

+loadbalancer and security groups

3. Create repo
aws ecr create-repository \
    --repository-name tod

4. Create ecr repository policy
aws ecr put-lifecycle-policy \
    --repository-name "tod" \
    --lifecycle-policy-text "file://repository_policy.json"

5.
aws ecs create-cluster \
    --cluster-name todCluster --capacity-providers FARGATE  

6. create service
aws ecs create-service \
    --cluster todCluster \
    --service-name todCluster \
    --task-definition sample-fargate:1 \
    --desired-count 1 \
    --launch-type FARGATE \
    --platform-version LATEST \
    --load-balancers
    --role
    --network-configuration "awsvpcConfiguration={subnets=[subnet-12344321],securityGroups=[sg-12344321],assignPublicIp=ENABLED}" \

7. create log group

8. iam user

9. add permissions to user + service linked role

10. create roles & permissions for ecs

Github actions
Create secrets
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
EXECUTION_ROLE_ARN

variables
AWS_REGION
ECR_REPOSITORY

sed -i 's|AWS_REGION|${{ vars.AWS_REGION }}|g; s|EXECUTION_ROLE_ARN|${{ secrets.EXECUTION_ROLE_ARN }}|g; s|CONTAINER_IMAGE|${{ needs.build.outputs.image }}|g' task_definition.json
        

Tear down
1. Delete VPC stack 
aws cloudformation delete-stack \
    --stack-name todstack

2. Delete cluster
aws ecs delete-cluster \
    --cluster todCluster 

3. Delete service

4. delete repository

delete log group
