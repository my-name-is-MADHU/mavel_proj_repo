FROM azul/zulu-openjdk:17-latest

WORKDIR /app

# Copy the JAR built by Maven
COPY target/my-maven-app-1.0-SNAPSHOT.jar app.jar

# Expose port 8080
EXPOSE 8080

# Run the JAR
CMD ["java", "-jar", "app.jar"]