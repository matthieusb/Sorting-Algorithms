# Project development tools for SpringBoot app
Here are a few instructions to install and use springboot

## How to build with maven
-----

### Install maven
SpringBoot works with maven 3.2. Install it through *apt* for ubuntu systems. Careful with a raspberry pi, an apt install does not necessarily give you the right version.

### Start the project
Use this link to create a template *pom.xml* : [Spring io starter generator](https://start.spring.io/)

[OR] use the following like to start from almost scratch : [Spring with maven](https://spring.io/guides/gs/maven/)


Then, go to your project home and use the following commands :

  - Compiling :

```
mvn compile
```
  - Testing :

```
mvn test
```

  - Packaging (with testing) :

```
mvn package
```  

  - Compile, test and package

```
mvn install
```  

To run it, just use the jar package as usual

### Running with maven springboot plugin
Add the following plugin to your *pom.xml* file :

```
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <version>1.4.3.RELEASE</version>
    <executions>
        <execution>
            <goals>
                <goal>repackage</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

And then, to run it :

```
mvn spring-boot:run
```

## SpringBoot CLI install
-----
First you need SDKMan installed on your machine
Go to this link : [SdkMan Website](http://sdkman.io/install.html). Then, run the following command to install springboot :
```
sdk install springboot
```

## How to use springboot CLI
----
Haven't used it yet
