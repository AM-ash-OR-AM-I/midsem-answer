## Sample Questions

### 1.⁠ ⁠List four key features of the Spring Boot framework

1. Simplified Configuration: Spring Boot eliminates boilerplate configurations required for Spring applications, allowing developers to focus on the application's concept rather than internal Java configuration.
    2. Production-Ready Features: Spring Boot provides production-ready features such as health checks, metrics, and externalized configuration, making it easy to deploy and manage applications.
    3. Auto-Configuration: Spring Boot automatically configures components based on classpath settings, reducing the need for manual configuration.
    4. Embedded Servers: Spring Boot includes embedded servers such as Tomcat, Jetty, and Undertow, making it easy to run and test applications without needing to deploy to a standalone server.

- Source: [22, 41, 21, 9]

### 2.⁠ ⁠Describe the purpose of Spring Boot starters. List and explain the Spring Boot starters for web and actuator functionalities

The purpose of Spring Boot starters is to provide a quick and easy way to add dependencies to a project, without having to manually configure them. These starter packs, when loaded into the classpath, automatically set up and configure various functionalities, making it easier for developers to focus on the core functionality of their application.

Some examples of Spring Boot starter dependencies include:

1. spring-boot-starter-web: This starter pack provides all the necessary dependencies for developing web applications, including Spring MVC, Tomcat, and Jackson, among others.

2. spring-boot-starter-actuator: This starter pack includes dependencies for monitoring and managing the application, such as health checks, metrics, and logging.

3. spring-boot-starter-security: This starter pack provides dependencies for securing the application by enabling features such as authentication and authorization.

4. spring-boot-starter-data-jpa: This starter pack includes dependencies for using Spring Data JPA, which allows for easy database access and manipulation.

5. spring-boot-starter-cache: This starter pack provides dependencies for using caching in the application, which can improve performance.

6. spring-boot-starter-aop: This starter pack includes dependencies for using Aspect-Oriented Programming (AOP), a technique for managing cross-cutting concerns in the application.

- Source: [65, 16, 9, 21]

### 3.⁠ ⁠Define dependency injection. Provide a code snippet illustrating constructor Injection using @Autowired and @Component annotations in a Spring Boot application

Dependency injection is a design pattern used in object-oriented programming where the dependencies of a component are provided externally instead of being created within the component itself. This removes the dependency of a component from the source code, making the code loosely coupled and easier to maintain. In a Spring Boot application, dependency injection is achieved using the @Autowired annotation.

Constructor Injection is a type of dependency injection where the dependencies are injected through a constructor. In a Spring Boot application, this can be achieved using @Autowired and @Component annotations as shown in the following code snippet:

// CPU class
package com.author.kickstart.model;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class CPU {

    private Harddisk harddisk;

    @Autowired
    public CPU(Harddisk harddisk) {
        this.harddisk = harddisk;
    }

    public String getInfo() {
        return "info";
    }
}

// AppConfig class
package com.author.kickstart.configuration;

import org.springframework.context.annotation.Configuration;
import com.author.kickstart.model.CPU;

@Configuration
public class AppConfig {

    @Autowired
    CPU cpu;
    
    public void getInfo() {
        System.out.println(cpu.getInfo());
    }
}

- Source: [88, 64, 89, 96]

### 4.⁠ ⁠Give an example demonstrating the use of the @PreDestroy' and '@PostConstruct annotations

    '''public class Car {

    private String model;
    private String color;

    public Car(String model, String color) {
        this.model = model;
        this.color = color;
    }

    @PostConstruct
    public void init() {
        System.out.println("Creating a new car: " + this.model + " in " + this.color);
    }

    @PreDestroy
    public void destroy() {
        System.out.println("Destroying a car: " + this.model);
    }
}

@Configuration
public class CarConfig {

    @Bean
    public Car car() {
        return new Car("Toyota", "Blue");
    }
}

public class Main {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(CarConfig.class);
        context.registerShutdownHook();
    }
}

Output:
Creating a new car: Toyota in Blue
Destroying a car: Toyota

In this example, the Car class is annotated with @PostConstruct and @PreDestroy annotations. The init() method is annotated with @PostConstruct and is invoked after the Car bean is created and added to the application context. Similarly, the destroy() method is annotated with @PreDestroy and is invoked before the Car bean is

- Source: [117, 97, 129, 96]

### 5.⁠ ⁠Explain lazy initialization with a suitable example. List its benefits

    Lazy initialization refers to the process of delaying the creation of objects until the point at which they are needed. In Java, this is achieved through the use of the @Lazy annotation. This annotation can be applied to classes, methods, or fields and allows for objects to be initialized only when they are explicitly called upon.

One example of lazy initialization can be seen in the use of the @Lazy annotation in conjunction with the @Autowired annotation. This allows for beans to be created and initialized only when they are needed, rather than at the startup of the application. For example, a CPU bean can be created and injected into another part of the application only when it is explicitly called for, rather than being created immediately at startup.

Some benefits of lazy initialization include improved performance and reduced resource usage. By delaying the creation of objects until they are needed, the application can run more efficiently and use fewer resources, resulting in a faster and more streamlined experience for the user. Additionally, lazy initialization can also help to prevent potential memory leaks by only creating objects when they are required, rather than having them constantly taking up space in the application.

- Source: [96, 97, 95, 147]

### 6.⁠ ⁠Define Spring Boot. What tools are requiried to build an application in spring boot?

1. Spring Boot is a comprehensive framework for developing production-ready applications that focuses on single functionality.
    2. JDK 8, Spring Tool Suite (STS), Spring Initializr, Apache Maven, Gradle are the tools required to build an application in Spring Boot.

- Source: [41, 9, 21, 15]

### 7.⁠ ⁠Which annotations are included in @SpringBootApplication?

The annotations included in @SpringBootApplication are:
    - @Component
    - @Configuration
    - @EnableAutoConfiguration
    - @ComponentScan

- Source: [118, 108, 64, 343]

### 8.⁠ ⁠How can we create our own auto-configuration class?

We can create our own auto-configuration classes by annotating them with the @Configuration annotation and ensuring that they are in the application's classpath. These classes can contain methods annotated with @Bean that will be automatically configured by Spring. Additionally, we can use the @EnableAutoConfiguration annotation to enable auto-configuration for our custom class.

- Source: [85, 81, 84, 289]

### 9.⁠ ⁠What is @Autowired and explain with example?

    @Autowired is an annotation used in the Spring framework to mark a constructor, field, or setter method to get autowired by Spring DI. This dependency injection technique removes the dependency of a component from the source code, making it loosely coupled and allowing for easier unit testing. 
    There are three types of autowiring in Spring: constructor, field, and setter method. 
    An example of autowiring a constructor is shown in the following code snippet: 

    package com.author.kickstart.model;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Component;
    @Component
    public class CPU {
        private Harddisk harddisk;
        @Autowired
        public CPU(Harddisk harddisk) {
            this.harddisk = harddisk;
        }
    }

    In the above example, the Harddisk dependency is autowired through the constructor, making it available for use in the CPU class. This is done by annotating the constructor with @Autowired. 
    Autowiring a field is shown in the following code snippet: 

    package com.author.kickstart.model;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Component;
    @Component
    public class CPU {
       
- Source: [88, 96, 89, 17]

### 10.⁠ ⁠Write an example using @Bean

    @Bean
    public CPU createCpu() {
        return new CPU("i5", 7);
    }

- Source: [88, 96, 101, 102]

### 11.(a) What is a Spring Boot Starter?Give some examples

A Spring Boot Starter is a dependency that provides a set of pre-configured dependencies and auto-configuration for a specific functionality in a Spring Boot application. Some examples of Spring Boot Starters are:

- spring-boot-starter-web: for developing web applications
- spring-boot-starter-data-jpa: for working with relational databases using Java Persistence API (JPA)
- spring-boot-starter-security: for securing web services and applications
- spring-boot-starter-test: for writing unit and integration tests in a Spring Boot application.
- Source: [41, 21, 22, 9]

### 11.(b) How do You Create a Spring Boot Application?

You can create a Spring Boot application by using the Spring Initializr tool provided by the Spring team. This tool offers the most commonly used dependencies for developing a Spring Boot application and generates a skeleton of your project.

- Source: [41, 15, 42, 9]

### 12.⁠ ⁠How do You Connect a Spring Boot Application to a database? Give example with an entity class and repository interface configuring the necessary setting in application.properties file

To connect a Spring Boot application to a database, you can use Spring Data JPA. Here's an example with an entity class and repository interface configuring the necessary settings in the application.properties file:

1. Entity class: Employee.java

@Entity
@Table(name = "employees")
public class Employee {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(name = "first_name")
  private String firstName;

  @Column(name = "last_name")
  private String lastName;

  @Column(name = "email")
  private String email;

  // getters and setters
}

2. Repository interface: EmployeeRepository.java

@Repository
public interface EmployeeRepository extends JpaRepository<Employee, Long> {

}

3. application.properties file:

```properties
# datasource configuration

spring.datasource.url=jdbc:mysql://localhost:3306/employeesdb
spring.datasource.username=root
spring.datasource.password=your_password
spring.datasource.driver-class-name=com.mysql.jdbc.Driver

# JPA configuration

spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

The above configuration will connect the Spring Boot application to a MySQL database named "employeesdb" with the specified username and password. The "ddl-auto" property is set to "update" which will create

- Source: [152, 119, 203, 20]

### 13.(a) What is Spring Boot DevTools?

Spring Boot DevTools is a Spring Boot feature that allows for automatic restarting of an application when files or classes are modified. It also provides a live reload option for templates and static content.

- Source: [41, 21, 9, 22]

### 13.(b) What is Spring Boot Autoconfiguration?

Spring Boot auto-configuration is a feature that automatically configures a Spring application based on the dependencies included in the classpath. This allows developers to easily create and use beans without having to explicitly configure them, making the development process more efficient. It is enabled by the @EnableAutoConfiguration annotation, which is present in the autoconfigure dependency under the package org.springframework.boot.autoconfigure.

- Source: [81, 16, 65, 84]

### 14.⁠ ⁠What is the difference between Spring and Spring Boot?

    Spring is a framework for developing both web and cloud-native applications, while Spring Boot is a framework built on top of Spring that eliminates boilerplate configurations required for Spring applications.

- Source: [41, 9, 21, 22]

### 15.⁠ ⁠What is dependency Injection in spring boot?Explain with proper example

Dependency injection is a design pattern used in Spring Boot to provide objects that an application needs to function. It is a way to achieve loose coupling between objects, meaning that objects are not tightly dependent on one another. Instead, the dependencies are injected into the objects at runtime, making the code more modular and easier to maintain.

One example of dependency injection in Spring Boot is the use of the @Autowired annotation. This annotation allows for automatic dependency injection by scanning the classpath for components that are annotated with @Component, @Service, or @Repository annotations. These components are then instantiated and injected into the class where @Autowired is used.

For example, we can create a UserService class that requires an instance of a UserRepository class to perform database operations. We can annotate the UserRepository class with @Repository and the UserService class with @Service. Then, in the UserService class, we can use the @Autowired annotation to inject an instance of the UserRepository class.

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    // methods that use the userRepository
}

@Repository
public class UserRepository {

    // database operations
}

This way, we can access the methods of the UserRepository class without having to instantiate it manually. This not only makes the code more modular but also allows for

- Source: [85, 43, 77, 73]

### 16.⁠ ⁠Discuss bean life cycle in detail

1. Creation: Bean life cycle begins with the creation of a bean instance. This is done by using the new keyword or by calling a factory method.
2. Initialization: Once the bean instance is created, the container initializes it by calling its setter methods and injecting any dependencies.
3. Using: The bean is now ready for use and can be called upon whenever needed.
4. Destruction: When the container is shut down or when the application context is closed, the bean is destroyed. This can also be done manually by calling the destroy() method on the bean.
5. Instantiation: During the instantiation phase, the container creates an instance of the bean. This can be done using the constructor or using a factory method.
6. Post-Initialization: Once the bean is instantiated, any post-processing can be done. This includes implementing the BeanPostProcessor interface and overriding the postProcessBeforeInitialization and postProcessAfterInitialization methods.
7. Destruction: This is the final phase of the bean life cycle. During this phase, the bean is removed from the container and any cleanup operations can be performed. This can be done by implementing the DisposableBean interface and overriding the destroy() method. Alternatively, a custom destroy method can be specified using the @Bean annotation.

- Source: [118, 16, 20, 41]

### 17.⁠ ⁠What is micro service? Discuss in brief

Microservice is an architectural design that creates scalable, loosely coupled, and testable applications which have a single function module with well-defined interfaces. Unlike traditional monolithic architecture, where all the code is contained within a single application, microservices break down the application into smaller, independent services that communicate with each other via APIs. Each microservice can be owned and maintained by a small team, making it easier to develop, test, and deploy new features. This design is adapted by many enterprises as it allows for faster and more agile development, with the ability to continuously deliver updates and enhancements.

- Source: [24, 22, 25, 153]

### 18.⁠ ⁠What are the advantages of Spring Boot over Spring?

1. Faster way of developing applications by reducing the boilerplate configurations.
2. Loosely coupled dependencies.
3. Starter packs available as part of dependency for simplifying builds and configuration.
4. Creating production-ready microservices with actuator health endpoints such as health, httptrace, mappings, metrics, info, configprops, env, and so on.
5. Embedded container server support. By default, Tomcat is used.
6. Auto-configuration for dependencies; once the dependency is loaded into the class path, Spring Boot manages the class instantiations, when needed.
7. Externalized configurations with the help of .properties and .yml files and Spring Cloud Config.
8. Live reload for the application during the development phase.
9. Ability to exclude/change the dependency version before deployment.
10. Simplifies the process of writing boilerplate code for complex software.
11. Allows developers to focus on the application's concept rather than on the internal Java configuration.
12. Can be executed by java –jar <jar name> just like any other Java project that builds a jar file.
13. Can also be started by running the mvn spring-boot:run command.
14. Need less Spring configuration compared to traditional Spring applications.

- Source: [22, 23, 9, 41]

### 19.⁠ ⁠Distinguish between constructor and setter based dependency

- Constructor-based Dependency: This type of dependency is based on the constructor injection method, where the dependencies are provided through the constructor of a class. The dependencies are injected while creating the instance of the class, and the values cannot be changed later on. This method is mostly used for mandatory dependencies.

- Setter-based Dependency: This type of dependency is based on the setter injection method, where the dependencies are provided through setter methods. The dependencies are injected after the instance of the class is created, and the values can be changed later on using the setter methods. This method is mostly used for optional dependencies.
- Source: [89, 85, 49, 43]

### 20.(a) Discuss the importance of loose coupling

Loose coupling is an architectural design pattern that promotes independence and flexibility between different components of a system. It is an important concept in software development as it allows for easier maintenance and scalability of the system.

One of the main benefits of loose coupling is that it reduces dependencies between components. This means that if one component needs to be changed or updated, it will not affect the other components of the system. This also makes it easier to replace or remove components without causing disruptions to the entire system.

Another advantage of loose coupling is that it promotes reusability of code. Components can be designed to be modular and independent, making it easier to reuse them in different parts of the system. This can save time and effort in development, as well as improve the overall quality of the code.

Loose coupling also allows for easier integration of new components into the system. Since each component is independent, it can be integrated without affecting the existing components. This is especially beneficial in large and complex systems where new components are constantly being added.

Moreover, loose coupling promotes better testing and debugging of the system. With components being independent, it is easier to isolate and test them individually, making it easier to identify and fix any issues.

Overall, loose coupling leads to a more flexible and resilient system.

- Source: [24, 250, 316, 38]

### (b) How are the @RestController and Controller Annotation different?

The @RestController and @Controller annotations serve different purposes in a Spring web application.

1. Function:

- The @RestController annotation is used to mark a class as the REST controller, which has a combination of @Controller and @ResponseBody features. This annotation is used at the top of a class.
- The @Controller annotation is used to mark a class as a controller, which handles the user's request and returns a response. This annotation is also used at the top of a class.

2. Return type:

- The methods in a class annotated with @RestController are assumed to return the response body directly, without any view resolution. This means that the return type of a method with @RestController annotation can be any Java object, and it will be converted to JSON/XML response by default.
- The methods in a class annotated with @Controller may return a String, a ModelAndView object, or any other type. These methods are responsible for returning the view to be rendered to the user.

3. Annotation:

- The @RestController annotation is a combination of @Controller and @ResponseBody annotations. This means that it is not necessary to use @ResponseBody annotation on methods with @RestController annotation, as it is implied.
- The @Controller annotation needs to be used in conjunction with @ResponseBody
- Source: [163, 105, 118, 104]

### 21.⁠ ⁠What is Spring Boot? Which tools are required to build an application in Spring Boot?

1. Spring Boot is a comprehensive way of developing production-ready applications focusing on single functionality.
    2. The tools required to build an application in Spring Boot are JDK 8, Spring Tool Suite (STS), Spring Initializr, Apache Maven, and Gradle.

- Source: [41, 21, 15, 9]

### 22.⁠ ⁠List out important features of Spring Boot. How to setup a Spring Boot Environment?

1. Auto-configuration: Spring Boot provides auto-configuration, which automatically configures the application based on the dependencies used.

2. Opinionated: Spring Boot follows an opinionated approach, which means it provides default configurations, but developers can override them if needed.

3. Embedded servers: Spring Boot comes with embedded servers, such as Tomcat, Jetty, and Undertow, which makes it easy to deploy and run applications without the need for external servers.

4. Production-ready: Spring Boot is designed to be production-ready, which means it includes features like health checks, metrics, and externalized configurations, making it easier to deploy and manage applications in a production environment.

5. Developer-friendly: Spring Boot is designed to be developer-friendly, which means it provides a simple and intuitive way to develop applications without the need for complex boilerplate code.

To set up a Spring Boot environment, you will need the following tools:

1. Java Development Kit 8 (JDK 8)
2. Build tool - Apache Maven or Gradle
3. Integrated Development Environment (IDE) - Spring Tool Suite (STS)
4. Spring Initializr - a web-based tool for generating Spring Boot projects
5. Dependencies - common dependencies required for developing an application in Spring Boot.

- Source: [41, 21, 15, 9]

### 23.⁠ ⁠List out features of the 12-factor app. Explain about "Minimal Viable Product" release of a software

1. Always use the latest versions of tools, Spring libraries, and other dependencies.
2. Strictly separate build and run stages.
3. Execute the app as one or more stateless processes.
4. Export services via port binding.
5. Scale out via the process model.
6. Maximize robustness with fast startup and graceful shutdown.
7. Keep developing, staging, and production as similar as possible.
8. Continuous deployment and continuous delivery.
9. Treat logs as event streams.
10. Run the app as one or more services.
11. Strictly separate build and run stages.
12. Use declarative formats for setup automation.
13. Have a clean contract with the operating system.
14. Keep development, staging, and production as similar as possible.
15. Minimize divergence between development and production.
16. Keep the build, release, and run stages separate.
17. Have a strict separation of configuration from code.
18. Use build, release, run to have a consistent deployment environment.
19. Use the 12-factor app to deploy software to a wide variety of environments.
20. Be able to scale out via the process model.
21. Maximize robustness with fast startup and graceful shutdown.
22. Keep development, staging,

- Source: [41, 24, 38, 336]

### 24.⁠ ⁠What is Spring Initialize? How Spring Initialize creates a Maven Spring Boot application skeleton?

Spring Initializr is a tool provided by the Spring team that allows developers to create a Maven Spring Boot application skeleton. It offers commonly used dependencies and configuration options, and generates a skeleton project that can be imported into an IDE. By selecting the desired dependencies and configurations, developers can quickly set up a Spring Boot project without having to manually configure all the necessary components.

- Source: [42, 9, 15, 21]

### 25.⁠ ⁠What is meant by microservices? Discuss about the advantageous features of Microservices which breaks the monolithic way of developing software. State some drawbacks of using microservices

Microservices is an architectural design that creates scalable, loosely coupled, and testable applications which have a single function module with well-defined interfaces. In contrast to the traditional monolithic approach, microservices break down a large application into smaller, independent services. Each service is built around a specific business capability and can be developed, tested, and deployed independently without impacting the entire application. These individual services communicate with each other through web services or APIs, allowing them to seamlessly share data and functionality.

Some of the advantageous features of using microservices over the monolithic approach include:

1. Scalability: Microservices allow for scaling individual services based on their specific needs, rather than scaling the entire monolithic application. This results in more efficient resource allocation and cost savings.

2. Loose Coupling: Each service in a microservices architecture is independent and can be developed and deployed separately. This allows for faster development and deployment cycles, and reduces the risk of system failures.

3. Flexibility: Since each service is independent, developers can choose the most suitable technology stack for each service. This allows for greater flexibility and the ability to use cutting-edge technologies.

4. Easier Maintenance: With microservices, any changes or updates can be made to a specific service without affecting the entire application. This

- Source: [24, 25, 22, 15]

### 26.⁠ ⁠How does a spring application get started?

    When a Spring Boot application is created, it automatically configures and starts an embedded server, such as Tomcat or Jetty. This allows the application to be run without any additional setup or configuration. The application can be started by running the main method in the application class, or by using the Spring Boot Maven/Gradle plugin.

- Source: [203, 85, 41, 120]

### 27.⁠ ⁠Is it possible to change the port of the embedded Tomcat server in Spring Boot? If yes then how to change it

Yes, it is possible to change the port of the embedded Tomcat server in Spring Boot by putting "server.port=8081" in application.properties file. This file is used to manage the configuration of the application. Another option is to use application.yml file where the configurations are specified with proper indentation. The preference is given to application.properties if both files are used.

- Source: [62, 85, 61, 38]

### 28.⁠ ⁠What is the use of the following annotations: @Autowired, @ComponentScan, @Bean

    - @Autowired: This annotation is used to mark a constructor, field, or setter method to be autowired by Spring DI. This enables dependency injection, which removes the dependency of a component from the source code, making it loosely coupled and allowing for easier unit testing.
    - @ComponentScan: This annotation is used to specify the packages that should be scanned by Spring for components, services, and repositories. It allows for automatic detection of Spring-managed beans within the specified packages.
    - @Bean: This annotation is used to declare a bean within the BeanFactory. It is usually placed on top of a method and can act as a replacement for the <bean> element in XML configuration. 

- Source: [88, 118, 64, 17]

### 29.⁠ ⁠What is the difference between @RequestMapping and @GetMapping?

    The @RequestMapping annotation is used to map HTTP web requests onto methods in classes that are annotated with @RestController or @Controller. It can be used at both the class and method level and supports all HTTP methods. On the other hand, the @GetMapping annotation is a specialized version of @RequestMapping for HTTP GET requests. It is used only at the method level and is a shortcut for @RequestMapping(method = RequestMethod.GET).

- Source: [105, 203, 163, 164]

### 30.⁠ ⁠What is an IOC container?

    An IOC container, or Inversion of Control container, is a design pattern used in software development to achieve loose coupling between components. It allows for the creation and management of objects and their dependencies, as well as the resolution of these dependencies at runtime. This enables more flexible and maintainable code.

- Source: [318, 324, 317, 336]

## Midterm Questions

### 1(a) What is Spring Boot? Which tools are required to build anapplication in Spring Boot

1(a) Spring Boot is a comprehensive way of developing production-ready applications focusing on single functionality. The tools required to build an application in Spring Boot include Java Development Kit 8, Apache Maven or Gradle, and Spring Tool Suite (STS).

- Source: [41, 15, 21, 9]

### (b) What is multiple inheritance by interface in JAVA. Explain itby using an example

    Multiple inheritance is a feature of object-oriented programming in which an object or class can inherit characteristics and features from more than one parent object or parent class. This allows the child object or class to have access to all the methods and properties of its parent classes.

        In Java, multiple inheritance is achieved through interfaces. An interface is a collection of abstract methods and constants that can be implemented by a class. A class can implement multiple interfaces, thus allowing for multiple inheritance.

        For example, in the given context, both the Car and Bike classes implement the Vehicle interface, which has a method for getting the number of wheels. This way, both the Car and Bike classes can access the getWheels() method and have their own implementations for it.

        This is a powerful feature as it allows for code reuse and promotes modularity in programming. However, it should be used with caution as it can lead to complex code and conflicts if not implemented properly. 

- Source: [98, 141, 126, 100]

### (c) Execute small JAVA collection programs for the List & Queue

You can write a simple Java program to demonstrate the usage of List and Queue collections in the following way:

    import java.util.List;
    import java.util.ArrayList;
    import java.util.Queue;
    import java.util.LinkedList;

    public class CollectionDemo {

        public static void main(String[] args) {

            // Example 1: List
            List<String> names = new ArrayList<>();
            names.add("John");
            names.add("Mary");
            names.add("Bob");
            names.add("Alice");
            names.add("Tom");

            System.out.println("Names: " + names);
            System.out.println("Size of names list: " + names.size());
            System.out.println("First name: " + names.get(0));
            System.out.println("Last name: " + names.get(names.size() - 1));

            // Example 2: Queue
            Queue<String> tasks = new LinkedList<>();
            tasks.add("Task 1");
            tasks.add("Task 2");
            tasks.add("Task 3");
            tasks.add("Task 4");
            tasks.add("Task 5");

            System.out.println("Tasks: " + tasks);
            System.out.println("Size of tasks queue: " + tasks.size());
            System.out.println("

- Source: [152, 314, 140, 56]

### 2.(a) List out features of the 12-factor app. Explain about "MinimalViable Product" release of a software

(a) The features of the 12-factor app are:

    1. Codebase: The codebase should be maintained in a version control system like Git or SVN.

    2. Dependencies: All dependencies should be declared explicitly and isolated from other dependencies.

    3. Config: Configuration should be stored in the environment.

    4. Backing services: Backing services such as databases, caches, and queues should be attached to the application as resources.

    5. Build, release, run: These stages should be strictly separated to ensure that the application can be built, released, and run independently.

    6. Processes: Applications should be executed as one or more stateless processes.

    7. Port binding: Services should be exported via port binding to allow for easy communication between applications.

    8. Concurrency: Applications should be able to scale out via the process model.

    9. Disposability: Applications should be easily disposed of to maximize robustness.

    10. Dev/prod parity: Development, staging, and production environments should be as similar as possible.

    11. Logs: Applications should produce logs as event streams.

    12. Admin processes: Admin tasks should be run as one-off

- Source: [41, 24, 336, 38]

### (b) What is Spring Initializi? How Spring Initializ creates aMaven Spring Boot application skeleton?

Spring Initializr is a tool provided by the Spring team to create a Maven Spring Boot application skeleton. It allows developers to quickly generate a project with all the necessary dependencies and configurations for a Spring Boot application. Spring Initializr creates this skeleton by generating a pom.xml file with all the required dependencies, such as Spring Boot starter, web, and test dependencies, and a basic project structure with a main application class annotated with @SpringBootApplication. The generated project can then be imported into an IDE and built using Maven or Gradle.

- Source: [42, 41, 64, 15]

### (c) What is meant by microservices? Discuss about theadvantageous features of Microservices, also mention some drawbacks of microservices

Microservices refer to a software architecture that breaks down a large monolithic application into smaller, independent services that communicate with each other through APIs. Each service is responsible for a specific functionality and can be developed, deployed, and managed independently.

Some advantageous features of microservices include:

1. Single functionality and data repository: Each service has a specific purpose, which makes it easier to understand and maintain. Data is managed separately for each service, which helps in scalability and performance.

2. Independent and isolated: Changes in one service do not affect the whole application. This enables faster development and deployment of new features.

3. Communication via APIs: Services communicate with each other using Inter-Process Communication (IPC) calls through web services/APIs. This allows data to be accessed from different services, making it easier to share and integrate data.

4. Independent testing: Each service can be tested independently, which saves time and effort compared to a monolithic application where the entire application needs to be tested even if only a small part has been changed.

5. Isolated deployment: Each service can be deployed independently in an isolated environment. This allows for better resource management and reduces the risk of downtime.

Some drawbacks of microservices include:

1. Increased cost: Each microservice runs in an

- Source: [24, 25, 22, 153]

### 3 (a) Write a simple Spring application, to understand the life of beans

The following is a simple Spring application that demonstrates the life of beans:

'''Preface
Spring is an excellent framework for developing both web and cloud-native
applications. This book on application development using Spring Boot
simplifies the process of writing boilerplate code for complex software. It
allows developers to concentrate on the application's concept rather than on
the internal Java configuration.

This book will guide you on how to make the best use of the strength that
Spring Boot provides. You'll gain an understanding of how Spring Boot
configuration works in conjunction with application development, including
auto-configuration and overriding default configurations. You will learn to
develop scalable, dependable microservices to accelerate the development
lifecycle of a cloud-based application. Each chapter will walk you through
the features of Spring Boot as a Software Development Framework, such as
performing Create, Read, Update, and Delete (CRUD) operations on a
database and securing web services with appropriate logging.

By the end of this book, you will develop, test, and deploy applications
ready for production and how to establish them as cloud-based applications.
The readers will also gain the expertise of writing unit and integration test
cases. Over the 12 chapters in this book, you will learn

- Source: [9, 41, 64, 156]

### (b) Describe the purpose of Spring Boot starters. List and explain Spring Boot starters for web and actuator functionalities

The purpose of Spring Boot starters is to provide a quick and easy way to add dependencies to a project and configure them automatically. This allows developers to focus on writing code instead of managing dependencies and configurations.

Some commonly used Spring Boot starters include:

1. spring-boot-starter-web - This starter includes all the necessary dependencies to create a web application, such as Tomcat, Spring MVC, and Spring Boot auto-configuration.

2. spring-boot-starter-actuator - This starter enables the actuator endpoints, which provide useful information about the application, such as health, metrics, and tracing.

3. spring-boot-starter-data-jpa - This starter includes all the dependencies necessary for using JPA (Java Persistence API) for database access, along with Spring Data, Hibernate, and Spring Boot auto-configuration.

4. spring-boot-starter-test - This starter includes all the necessary testing dependencies, such as JUnit, Mockito, and Spring Test.

5. spring-boot-starter-security - This starter enables security features, such as authentication and authorization, by including Spring Security and Spring Boot auto-configuration.

6. spring-boot-starter-cache - This starter provides support for caching by including Spring Cache and Spring Boot auto-configuration.

7. spring-boot-starter-aop

- Source: [65, 16, 22, 21]

### (c) Which annotations are included in @SpringBootApplication?Explain it by example

The annotations included in @SpringBootApplication are @SpringBootConfiguration, @EnableAutoConfiguration, and @ComponentScan. These annotations are used to configure and bootstrap the Spring Boot application.

For example, if we have a class named "MyApplication" annotated with @SpringBootApplication, it is equivalent to annotating it with the following annotations:

@SpringBootApplication
@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan

This reduces the amount of code needed to configure the application and allows for a more streamlined approach.

- Source: [108, 64, 118, 60]

### 4(a) Define a simple Spring Bean and explain how to configure iusing XML. For example, answer should show a class annotated as a bean and a corresponding XMI configuration file

    The following is an example of a simple Spring bean and its configuration using XML:

    Step 1: Create a Java class annotated with @Component to mark it as a Spring bean.

    @Component
    public class Student {
        private String name;
        private int age;

        //getters and setters
    }

    Step 2: Create an XML configuration file with the bean definition.

    <beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd">

        <bean id="student" class="com.example.Student">
            <property name="name" value="John Doe"/>
            <property name="age" value="20"/>
        </bean>
    </beans>

    In the above configuration, the <bean> tag defines a bean with the id "student" and class "com.example.Student". The <property> tags are used to set the values for the name and age properties of the Student bean.

    Step 3: Load the XML configuration file in the ApplicationContext.

    ApplicationContext context = new

- Source: [118, 88, 16, 64]

### (b)Write a Java Program to demonstrate annotation-based Java configuration UserRepository class with a method saveUser

package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class UserRepository {

 @Autowired
 private User user;

 public void saveUser() {
  System.out.println("Saving user: " + user);
 }
}

- Source: [129, 140, 124, 128]

### (c)Write POJO Java program to convert tightly coupled code intoloosely coupled code to: Create a parent class A with a method display(). Create another class B that inherits class A and contains a method display. Create a main class to call the display method

```java
public class Main {
    public static void main(String[] args) {
        A objA = new B();
        objA.display();
    }
}

class A {
    public void display() {
        System.out.println("This is a method from class A");
    }
}

class B extends A {
    @Override
    public void display() {
        System.out.println("This is a method from class B");
    }
}
```

- Source: [157, 98, 126, 316]

### 5.(a) Demonstrate how to configure an application property inapplication.properties and read it using @Value. For example,answer should include setting a property in application.properties and reading it in a class

    application.properties:
    my.application.property=test
    
    Class to read property using @Value:
    @Component
    public class MyClass {
        @Value("${my.application.property}")
        private String myProperty;
        
        public void printProperty() {
            System.out.println(myProperty);
        }
    }
    
    Output:
    test

- Source: [62, 203, 85, 94]

### (b)Give an example demonstrating the use of the @PreDestroyand "@PostConstruct annotations

    public void destroy() {
        connection.close();
    }

    @PostConstruct
    This annotation when used on top of methods notifies the container to invoke
    the method whenever the bean instantiation is completed for any initialization
    to bean properties. This method must be invoked before the class is put into
    service. In earlier examples, we have seen the usage of @Primary  and
    @Qualifier . Here, we used this annotation to get invoked after the bean is
    created successfully with all of its dependencies injected. Here is the snippet:
    package com.author.kickstart.service;
    import javax.annotation.PostConstruct;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.context.annotation.Configuration;
    import com.author.kickstart.interfaces.Vehicle;
    @Configuration
    public class VehicleService {
        @Autowired
        Vehicle vehicle;
        @PostConstruct
        public void service() {
            System.out.println("Wheels for vehicle:" + vehicle.getWheels());
        }
    }

    Conclusion
    In this chapter, we discussed a lot of annotations which would be surely
    useful when developing a Spring Boot application. There will be more sets
    of annotations that will be explained in the upcoming chapters along with

- Source: [117, 97, 129, 96]

### (c)Create a package of 4 classes named as address, Teacher, app,javaConfig. Address has fields as houseNo, city, postOffice, pin, state. Use setter method for the given fields and toString method to printstring representation of the object. Teacher class has name, id, mobileNo, and address fields. Use the setter method and toString method for this class. javaConfig class is java annotation-based configuration file which creates two address beans, and oneteacher bean and initialize the fields of both classes. In teacher class use any one address by using @Qualifier annotation. Call the teacher object in app class which consists of main method of Spring application

```java
package com.example;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class JavaConfig {
 
 @Bean
 public Address address1() {
  Address address = new Address();
  address.setHouseNo("123");
  address.setCity("New York");
  address.setPostOffice("NYC");
  address.setPin(12345);
  address.setState("New York");
  return address;
 }
 
 @Bean
 public Address address2() {
  Address address = new Address();
  address.setHouseNo("456");
  address.setCity("Los Angeles");
  address.setPostOffice("LA");
  address.setPin(67890);
  address.setState("California");
  return address;
 }
 
 @Bean
 public Teacher teacher() {
  Teacher teacher = new Teacher();
  teacher.setName("John Doe");
  teacher.setId(1);
  teacher.setMobileNo("123-456-7890");
  
  // Using @Qualifier annotation to choose one of the two address beans
  // Uncomment one of the following lines to choose the desired address
  //teacher.setAddress(address1());
```
- Source: [98, 97, 100, 157]
