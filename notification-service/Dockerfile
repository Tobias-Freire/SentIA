# 1: Build JAR
FROM maven:3.9.6-eclipse-temurin-21 AS build
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

# 2: Final image
FROM openjdk:21-jdk-slim
WORKDIR /app
COPY --from=build /app/target/notification-service-0.0.1-SNAPSHOT.jar /app/notification-service.jar
EXPOSE 8080
CMD ["java", "-jar", "/app/notification-service.jar"]