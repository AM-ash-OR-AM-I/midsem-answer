### 1.⁠ ⁠List four key features of the Spring Boot framework

1. Auto-configuration
2. Embedded servlet container
3. Production-ready features
4. Simplified development process

- Source: [22, 41, 21, 9]

### 2.⁠ ⁠Describe the purpose of Spring Boot starters. List and explain the Spring Boot starters for web and actuator functionalities

The purpose of Spring Boot starters is to provide a convenient way to include and configure common dependencies in a Spring Boot application. These dependencies, also known as starter packs, can be easily added to the classpath and automatically configured through auto-configuration.

Some of the Spring Boot starters for web and actuator functionalities include:

1. spring-boot-starter-web: This starter pack includes all the necessary dependencies for developing a web application using Spring Boot. It includes features such as embedded Tomcat server, Spring MVC, and Spring Boot auto-configuration for web development.

2. spring-boot-starter-actuator: This starter pack provides production-ready features for monitoring and managing the application. It includes endpoints for health checks, metrics, tracing, and more.

3. spring-boot-starter-data-jpa: This starter pack is used for developing applications that require database access. It includes Spring Data JPA and Hibernate dependencies, along with auto-configuration for database connection and transaction management.

4. spring-boot-starter-security: This starter pack provides security features for the application, such as authentication and authorization. It includes Spring Security and auto-configuration for securing endpoints and resources.

5. spring-boot-starter-cache: This starter pack includes caching dependencies, such as Spring Cache and Redis, for

- Source: [65, 16, 9, 21]

### 3.⁠ ⁠Define dependency injection. Provide a code snippet illustrating constructor Injection using @Autowired and @Component annotations in a Spring Boot application

Dependency injection is a technique used in software engineering to remove the hard-coded dependencies between objects. In this technique, the dependencies are injected into the objects at runtime, thus making the code loosely coupled and easier to maintain. In the Spring framework, dependency injection is achieved through the use of annotations like @Autowired, @Component, and @Configuration.

Below is an example of constructor injection using @Autowired and @Component annotations in a Spring Boot application:

// CPU class with a constructor that has a dependency on Harddisk class
package com.author.kickstart.model;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component // marks the class as a bean that can be managed by the Spring container
public class CPU {
    private Harddisk harddisk;

    @Autowired // injects the dependency of Harddisk class
    public CPU(Harddisk harddisk) {
        this.harddisk = harddisk;
    }
}

// Harddisk class
package com.author.kickstart.model;
import org.springframework.stereotype.Component;

@Component // marks the class as a bean that can be managed by the Spring container
public class Harddisk {
    // class definition
}

// Config class to define the beans
package com.author.kickstart.configuration;
import org.springframework

- Source: [88, 64, 89, 96]

### 4.⁠ ⁠Give an example demonstrating the use of the @PreDestroy' and '@PostConstruct annotations

The following example demonstrates the use of the @PreDestroy and @PostConstruct annotations:

```java
package com.example.demo;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

import org.springframework.stereotype.Component;

@Component
public class DatabaseConnection {

 @PostConstruct
 public void initializeConnection() {
  System.out.println("Initializing database connection...");
 }
 
 @PreDestroy
 public void closeConnection() {
  System.out.println("Closing database connection...");
 }
} 
```

In this example, we have a DatabaseConnection class with two methods annotated with @PostConstruct and @PreDestroy. The initializeConnection() method is annotated with @PostConstruct and will be executed after the bean is instantiated and its dependencies are injected. Similarly, the closeConnection() method is annotated with @PreDestroy and will be executed before the bean is destroyed.

Now, if we run this application and instantiate the DatabaseConnection bean, we will see the following output:

Initializing database connection...
Closing database connection...

This confirms that the @PostConstruct and @PreDestroy annotations were executed appropriately.

- Source: [117, 97, 129, 96]

### 5.⁠ ⁠Explain lazy initialization with a suitable example. List its benefits

Lazy initialization is a technique where an object is not created until it is actually needed. In other words, the object is not loaded into memory until it is used or referenced in the code. This is achieved by using the @Lazy annotation in Spring Boot applications.

For example, let's say we have a class called CPU that is annotated with @Component and has a method called getInfo(). We also have a class called AppConfig that has a @Lazy annotation on the CPU bean. In this scenario, the CPU bean will not be created during the application startup. Instead, it will be created only when it is explicitly autowired or referenced in the code.

One of the main benefits of lazy initialization is improved performance. By not creating objects until they are needed, the application uses less memory and has faster startup times. This can be especially useful in larger applications with many beans and dependencies.

Another benefit is increased flexibility. With lazy initialization, beans can be loaded and initialized on demand, which allows for more dynamic and efficient usage of resources. This can also help in managing complex dependency graphs and avoiding circular dependencies.

Overall, lazy initialization can be a useful technique in managing memory and improving performance in Spring Boot applications.

- Source: [96, 97, 95, 147]

### 6.⁠ ⁠Define Spring Boot. What tools are requiried to build an application in spring boot?

1. Spring Boot is a comprehensive way of developing production-ready applications focusing on single functionality.
2. Features of Spring Boot include auto-configuration, starter dependencies, and containerless deployment.
3. The tools required to build an application in Spring Boot include JDK 8, Spring Tool Suite (STS), Spring Initializr, Apache Maven, and Gradle.

- Source: [41, 9, 21, 15]

### 7.⁠ ⁠Which annotations are included in @SpringBootApplication?

@ComponentScan, @Configuration, @EnableAutoConfiguration

- Source: [118, 108, 64, 343]

### 8.⁠ ⁠How can we create our own auto-configuration class?

We can create our own auto-configuration class by creating a class annotated with the @Configuration annotation and defining a bean method annotated with @ConditionalOnMissingBean. This will ensure that the bean is only created if it does not already exist in the ApplicationContext. We can also use other conditional annotations such as @ConditionalOnClass, @ConditionalOnProperty, or @ConditionalOnBean to further customize the auto-configuration.

- Source: [85, 81, 84, 289]

### 9.⁠ ⁠What is @Autowired and explain with example?

@Autowired is an annotation that is used to mark a constructor, field, or setter method to get autowired by Spring DI. Dependency Injection is a technique that removes the dependency of a component from the source code so that our source code is loosely coupled with the component. This also makes unit testing possible. The Spring framework provides two ways of dependency injection – constructor and setter method.

An example of @Autowired is shown in the code snippet below:

package com.author.kickstart.model;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class CPU {

  @Autowired
  private Harddisk harddisk;
  
  // constructor
  public CPU() {
  
  }
  
  // setter method
  public void setHarddisk(Harddisk harddisk) {
    this.harddisk = harddisk;
  }
  
  // other methods
  // ...
  
}

In the above example, the Harddisk object is automatically injected into the CPU class using the @Autowired annotation. This allows the CPU class to access the Harddisk object without explicitly creating it, making the code more flexible and maintainable.

- Source: [88, 96, 89, 17]

### 10.⁠ ⁠Write an example using @Bean

```java
package com.author.kickstart.configuration;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import com.author.kickstart.model.CPU;
@Configuration
public class Config {
    @Bean(“cpu”)
    public CPU createCpu() {
        return new CPU(“i5”, 7);
    }
}
```

- Source: [88, 96, 101, 102]

### 11.(a) What is a Spring Boot Starter?Give some examples

(a) A Spring Boot Starter is a dependency that simplifies the process of setting up and configuring a specific feature or functionality in a Spring Boot application. It includes all the necessary dependencies and configurations for that particular feature. Examples of Spring Boot Starters include "spring-boot-starter-web" for creating web applications, "spring-boot-starter-data-jpa" for working with databases, and "spring-boot-starter-security" for implementing security features.

- Source: [41, 21, 22, 9]

### 11.(b) How do You Create a Spring Boot Application?

You can create a Spring Boot application by using the Spring Initializr tool provided by the Spring team. This tool offers commonly used Spring Boot dependencies and allows you to configure them easily for auto-configuration.

- Source: [41, 15, 42, 9]

### 12.⁠ ⁠How do You Connect a Spring Boot Application to a database? Give example with an entity class and repository interface configuring the necessary setting in application.properties file

To connect a Spring Boot Applicaiton to a database, you can use Spring Data JPA and configure the necessary settings in the application.properties file. For example, if we have an entity class called "User" and a repository interface called "UserRepository", we can configure the database connection in the application.properties file as follows:

```
spring.datasource.url=jdbc:mysql://localhost:3306/mydatabase
spring.datasource.username=username
spring.datasource.password=password
```

In the User entity class, we can specify the table name and column names with the @Table and @Column annotations. For example:

```java
@Entity
@Table(name = "users")
public class User {

  @Id
  @GeneratedValue(strategy = GenerationType.AUTO)
  private Long id;

  @Column(name = "username")
  private String username;

  @Column(name = "email")
  private String email;

  //getters and setters
}
```

In the UserRepository interface, we can define methods for interacting with the database using Spring Data JPA's query methods. For example:

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
  User findByUsername(String username);
  List<User> findByEmailContaining(String keyword);
}
```

This way, we can connect our Spring Boot application to a database and perform CRUD operations on the

- Source: [152, 119, 203, 20]

### 13.(a) What is Spring Boot DevTools?

Spring Boot DevTools is a set of tools that improves the development experience of Spring Boot applications. It includes features such as automatic application restart, live reload of static resources, and remote debugging.

- Source: [41, 21, 9, 22]

### 13.(b) What is Spring Boot Autoconfiguration?

Spring Boot autoconfiguration is a feature provided by the Spring Boot framework that automatically configures a Spring application based on the dependencies included in the classpath. This makes development easier for developers by creating and managing beans explicitly and using them in the application. This feature uses annotations such as @EnableAutoConfiguration, @ConditionalOnClass, @ConditionalOnBean, and @ConditionalOnProperty to determine when and how to configure beans and classes.

- Source: [81, 16, 65, 84]

### 14.⁠ ⁠What is the difference between Spring and Spring Boot?

    Spring is a Java-based framework that simplifies the process of writing boilerplate code for complex software. It requires developers to remember both configurations for the Spring model as well as the servlet container on which they are executing their application. On the other hand, Spring Boot is an open-source Java-based framework used to create standalone microservices with production-ready features. It eliminates the need to remember both configurations and allows developers to focus on the application's concept.

- Source: [41, 9, 21, 22]

### 15.⁠ ⁠What is dependency Injection in spring boot?Explain with proper example

Dependency Injection (DI) is a design pattern in Spring Boot that allows developers to leverage the benefits of loose coupling. It is a process of providing an object with its dependencies instead of creating them within the object itself. This allows for easier maintenance, testing, and scalability of the code.

One example of dependency injection in Spring Boot is the use of the @Autowired annotation. This annotation allows developers to inject dependencies into a class without having to manually create them. For example, in a controller class, we can use @Autowired to inject a service class that handles the business logic for our application.

@Controller
public class UserController {
    @Autowired
    private UserService userService;
    // other controller methods
}

In this example, Spring Boot will automatically create an instance of the UserService class and inject it into the UserController. This allows the controller to use the methods and functionality of the UserService without having to manually create an instance of it.

This dependency injection method allows for easier testing as well. In our unit tests, we can create a mock version of the UserService and inject it into our controller to test its functionality without having to access the actual database or external services.

Overall, dependency injection in Spring Boot helps to improve modularity, maintainability, and testability of our code. It follows

- Source: [85, 43, 77, 73]

### 16.⁠ ⁠Discuss bean life cycle in detail

Bean life cycle in Spring is the process of creating, initializing, using, and destroying a bean. It involves several steps that are performed in a specific order. These steps are defined by the Spring framework and cannot be modified by the user.

The following are the different stages of the bean life cycle in Spring:

1. Instantiation: This is the first stage of the bean life cycle where the Spring container creates an instance of the bean using its constructor or a factory method.

2. Populate properties: Once the bean is instantiated, the Spring container injects values into its properties and dependencies using dependency injection.

3. BeanNameAware and BeanFactoryAware: The Spring container calls the BeanNameAware and BeanFactoryAware interfaces to provide the bean with its name and reference to the BeanFactory.

4. Pre-initialization (PostConstruct): This stage allows the bean to perform any initialization tasks before it is ready for use.

5. InitializingBean and init-method: The Spring container calls the InitializingBean interface's afterPropertiesSet() method or the init-method specified in the bean's configuration to perform any further initialization tasks.

6. Ready for use: Once the bean has been initialized, it is now ready for use by the application.

7. Pre-destroy (PreDestroy):

- Source: [118, 16, 20, 41]

### 17.⁠ ⁠What is micro service? Discuss in brief

A microservice is a software architecture design where an application is composed of small, independent services that work together to perform a specific business function. Each service is decoupled and can be developed, deployed, and maintained independently. This allows for faster development, testing, and deployment of new features, as well as easier scalability and better fault tolerance. Microservices are typically owned and maintained by small teams, making it easier to manage and update the application. Microservices also promote a more agile development process, where new features can be continuously developed, tested, and delivered.

- Source: [24, 22, 25, 153]

### 18.⁠ ⁠What are the advantages of Spring Boot over Spring?

1. Faster development: Spring Boot reduces boilerplate code and simplifies the configuration process, allowing developers to focus on the application's concept rather than internal Java configurations. This leads to faster development and deployment.

2. Loosely coupled dependencies: Spring Boot's auto-configuration feature manages class instantiations, reducing the need for developers to manually configure dependencies.

3. Production-ready features: Spring Boot provides features such as actuator health endpoints, embedded container server support, and externalized configurations that make it easier to develop production-ready microservices.

4. Simplified builds and configurations: Spring Boot offers starter packs for common dependencies, simplifying the build process and reducing the need for developers to write configurations.

5. Live reload during development: Spring Boot automatically reloads the application during development, allowing for faster testing and debugging.

6. External dependency management: Spring Boot manages external dependencies, such as database access and external API calls, making it easier for developers to focus on the core functionality of their application.

7. Easy deployment: Spring Boot applications can be easily executed using the "java -jar" command, making it simple to deploy and run the application on any environment with a JVM.

8. Small team ownership: Microservices created using Spring Boot can be easily owned and maintained

- Source: [22, 23, 9, 41]

### 19.⁠ ⁠Distinguish between constructor and setter based dependency

    Constructor based dependency injection is a type of dependency injection in which dependencies are passed into an object through its constructor. In this way, the constructor serves as a way to "inject" dependencies into the object. This approach is commonly used in languages like Java and C#.

    Setter based dependency injection, on the other hand, is a type of dependency injection in which dependencies are set or "injected" into an object through setter methods. This approach is commonly used in languages like JavaScript and Python.

    In summary, the main difference between the two approaches is the way in which dependencies are provided to an object - through the constructor or through setter methods.

- Source: [89, 85, 49, 43]

### 20.(a) Discuss the importance of loose coupling

Loose coupling is a design principle in software development that refers to the degree of dependency between different components or modules of a system. It is important because it allows for a more flexible and maintainable system.

1. Flexibility: Loose coupling allows for changes to be made to one component without affecting other components. This means that new features or changes can be implemented without having to make extensive modifications to the entire system.

2. Modularity: By decoupling components, the system is divided into smaller, independent modules. This makes it easier to manage and maintain the codebase, as each module can be developed, tested and deployed separately.

3. Scalability: Loose coupling allows for components to be added or removed without impacting the overall functionality of the system. This makes it easier to scale the system as needed, without having to make significant changes to the existing codebase.

4. Reusability: By breaking down the system into smaller, independent components, these components can be reused in other applications. This saves time and effort in development, and also ensures consistency and avoids duplication of code.

5. Testability: A loosely coupled system is easier to test, as the components can be tested independently without having to rely on other components. This makes it easier to identify and

- Source: [24, 250, 316, 38]

### (b) How are the @RestController and Controller Annotation different?

The @RestController annotation is a combination of the @Controller and @ResponseBody annotations, which is used to create REST APIs. It is used at the top of a class and can also be used at the method level to define specific mappings for different HTTP methods.

On the other hand, the @Controller annotation is used to mark a class as a controller, which is responsible for handling web requests. It can also be used in combination with @ResponseBody to return data in a specific format.

In summary, the main difference between the two is that @RestController is specifically used for creating REST APIs, while @Controller is used for handling web requests in a web application.

- Source: [163, 105, 118, 104]

### 21.⁠ ⁠What is Spring Boot? Which tools are required to build an application in Spring Boot?

1. Spring Boot is a framework developed on top of the Spring framework that eliminates boilerplate configurations required for Spring applications.
    2. The tools required to build an application in Spring Boot are JDK 8, Spring Tool Suite (STS), Spring Initializr, and build tools like Maven and Gradle.

- Source: [41, 21, 15, 9]

### 22.⁠ ⁠List out important features of Spring Boot. How to setup a Spring Boot Environment?

1. Simplifies boilerplate code
2. Auto-configuration
3. Standalone applications
4. Production-ready applications
5. Embedded server
6. Easy dependency management
7. Actuator for monitoring and managing applications
8. Spring Boot CLI for creating and testing applications
9. Easily customizable
10. No need for XML configurations
11. Easy integration with other Spring projects
12. Simplified logging
13. Developer productivity
14. Spring Initializr for creating projects
15. Easy testing
16. Improved security features
17. Easy deployment
18. Cloud-native support
19. Easy conversion of existing Spring projects to Spring Boot
20. Community support and frequent updates.

To set up a Spring Boot environment, the following tools are required:

1. Java Development Kit (JDK) 8 or higher
2. Spring Tool Suite (STS) or any other IDE
3. Spring Initializr
4. Build tools such as Maven or Gradle
5. Apache Maven or Gradle for build automation.

- Source: [41, 21, 15, 9]

### 23.⁠ ⁠List out features of the 12-factor app. Explain about "Minimal Viable Product" release of a software. (Wrongs)

TL;DR
Refer: <https://12factor.net>

(fixed manually gave wrong ans)

- Codebase: One codebase tracked in revision control, many deploys
- Dependencies: Explicitly declare and isolate dependencies
- Config: Store config in the environment
- Backing services: Treat backing services as attached resources
- Build, release, run: Strictly separate build and run stages
- Processes: Execute the app as one or more stateless processes
- Port binding: Export services via port binding
- Concurrency: Scale out via the process model
- Disposability: Maximize robustness with fast startup and graceful shutdown
- Dev/prod parity: Keep development, staging, and production as similar as possible
- Logs: Treat logs as event streams
- Admin processes: Run admin/management tasks as one-off processes

- Source: [41, 24, 38, 336]

### 24.⁠ ⁠What is Spring Initialize? How Spring Initialize creates a Maven Spring Boot application skeleton?

Spring Initializr is a tool provided by the Spring team that allows developers to create a Maven or Gradle Spring Boot application skeleton. This tool provides a common structure and initial dependencies for the application, which can then be customized and built upon by the developer. To create a Maven Spring Boot application skeleton, developers can select the desired dependencies and project settings in Spring Initializr, and then download and import the generated project into their development environment.

- Source: [42, 9, 15, 21]

### 25.⁠ ⁠What is meant by microservices? Discuss about the advantageous features of Microservices which breaks the monolithic way of developing software. State some drawbacks of using microservices

Microservices is an architectural design approach in which a single application is broken down into smaller, independent services that communicate with each other using web services/APIs. These services are self-contained and can be deployed and tested independently. This approach aims to create scalable, loosely coupled, and testable applications with well-defined interfaces.

Advantages of Microservices:

1. Single Functionality and Data Repository: Each service in microservices has a single functionality and data repository, which makes it easier to understand and maintain. This also allows for better scalability as each service can be scaled independently.

2. Independent Services: In a monolithic architecture, a change in one part of the application can impact the whole application. Microservices, on the other hand, are independent of each other, so a change in one service does not affect the others.

3. Inter-Process Communication: Microservices communicate with each other using Inter-Process Communication (IPC) calls via web services/APIs. This allows for better data accessibility as one service can access data owned by another service.

4. Independent Testing: Each service in microservices can be tested independently, unlike in a monolithic architecture where the whole application needs to be tested even if only a small part has changed. This saves time and resources.

5

- Source: [24, 25, 22, 15]

### 26.⁠ ⁠How does a spring application get started?

The spring.application.name is specified whenever you create a Spring Boot application. The Eureka service discovery then discovers the application based on the application name.

- Source: [203, 85, 41, 120]

### 27.⁠ ⁠Is it possible to change the port of the embedded Tomcat server in Spring Boot? If yes then how to change it

Yes, it is possible to change the port of the embedded Tomcat server in Spring Boot. This can be done by adding the following line in the `application.properties` file:

```
server.port= <desired port number>
```

Alternatively, you can also change the port by adding the following line in the `application.yml` file:

```
server:
    port: <desired port number>
```

Please note that if both `application.properties` and `application.yml` files are present, the preference will be given to `application.properties`.

- Source: [62, 85, 61, 38]

### 28.⁠ ⁠What is the use of the following annotations: @Autowired, @ComponentScan, @Bean

The @Autowired annotation is used to mark a constructor, field, or setter method to be autowired by Spring DI. This allows for dependency injection, which removes the dependency of a component from the source code and makes it loosely coupled. It also enables unit testing.

The @ComponentScan annotation is used to specify the packages that should be scanned for Spring components, such as beans, controllers, and services. This allows for automatic detection and registration of these components in the ApplicationContext.

The @Bean annotation is used to declare a bean within the BeanFactory. This annotation can be used on top of a method and can act as a replacement for the <bean/> element in XML configuration. It supports attributes such as initMethod, destroyMethod, and autowireCandidate. By default, the bean name is the same as the method name unless specified otherwise.

- Source: [88, 118, 64, 17]

### 29.⁠ ⁠What is the difference between @RequestMapping and @GetMapping?

@GetMapping is a shortcut for @RequestMapping(method = RequestMethod.GET), which means it is used specifically for GET requests. @RequestMapping is a more general annotation used for mapping HTTP requests to methods, and it can handle all types of HTTP methods.

- Source: [105, 203, 163, 164]

### 30.⁠ ⁠What is an IOC container?

An IOC container is a core feature of the Spring framework. It is responsible for managing the creation and lifecycle of objects (beans) in a Spring application. The container uses dependency injection to wire together different components and manage their dependencies, making it easier to develop and maintain applications.

- Source: [318, 324, 317, 336]
