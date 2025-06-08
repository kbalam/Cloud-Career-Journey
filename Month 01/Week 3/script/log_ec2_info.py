import os

script__dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script__dir, "output")


#Dummy Info for logging.
ec2_info = {
    "InstanceId": "i-0abc123def456gh78",
    "InstanceType": "t2.micro",
    "State": "running",
    "LaunchTime": "2025-06-02T10:05:00Z",
    "AvailabilityZone": "ap-south-1a"
}


os.makedirs(output_dir, exist_ok=True)

with open (os.path.join(output_dir, "ec2_info.txt"), "w") as f:
    for key, value in ec2_info.items():
        f.write(f"{key}: {value}\n")

print("✅ EC2 info logged successfully to output/ec2_info.txt")
