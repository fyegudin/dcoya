# Import necessary modules
import subprocess

# Define JMeter test plan file
jmeter_test_plan = "infra/test-plan.jmx"

# Define JMeter command
jmeter_command = [
    "jmeter",  # Path to JMeter executable
    "-n",  # Non-GUI mode
    "-t", jmeter_test_plan,  # Path to test plan file
    "-l", "test-results.jtl",  # Path to save test results
    "-e",  # Generate dashboard report
    "-o", "dashboard"  # Path to save dashboard report
]

# Execute JMeter command
try:
    subprocess.run(jmeter_command, check=True)
    print("Stress test completed successfully. Test results and dashboard report generated.")
except subprocess.CalledProcessError as e:
    print("Error executing JMeter command:", e)
