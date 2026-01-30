import subprocess

mvn_path = r"C:\Program Files\maven-mvnd-1.0.3-windows-amd64\mvn\bin\mvn.cmd"  # <- note .cmd for Windows
command = [
    mvn_path,
    "archetype:generate",
    "-DgroupId=com.example",
    "-DartifactId=my-maven-app",
    "-DarchetypeArtifactId=maven-archetype-quickstart",
    "-Dversion=1.0-SNAPSHOT",
    "-Dpackage=com.example",
    "-DinteractiveMode=false"
]

subprocess.run(command, check=True)
