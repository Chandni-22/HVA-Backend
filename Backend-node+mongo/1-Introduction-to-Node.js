// 1.) What is Node.js?
/* Node.js is a JavaScript runtime environment that allows you to run JavaScript code on the server side, outside of a web browser. It is built on the V8 JavaScript engine, the same engine that powers Google Chrome, and provides a platform for building scalable, high-performance applications. Node.js is widely used for building server-side applications, APIs, and even full-stack web applications.

--> Overview of Node.js and Its Purpose:
# Node.js enables you to use JavaScript to write both client-side and server-side code, unifying your development stack. It is built to handle real-time applications like chat servers, APIs, or any application that requires high concurrency or quick responses to requests.

# Main Features of Node.js:
i) Event-driven: Uses an event-driven architecture, which means that Node.js can handle multiple connections simultaneously by using an event loop.

ii) Non-blocking I/O: Node.js performs I/O operations (such as reading files, querying databases) asynchronously, making it more efficient and faster.

iii) Single-threaded: Although Node.js is single-threaded, it can handle many requests at once using non-blocking I/O operations.

iv) Cross-platform: Node.js works across multiple platforms, including Windows, macOS, and Linux.

# Purpose: Node.js is ideal for building high-performance, real-time applications like:
i) Web servers

ii) RESTful APIs

iii) Real-time chat applications

iv) Streaming services

--> Understanding the Event-driven, Non-blocking I/O Model
# Event-driven:
Node.js operates on an event-driven model. The event loop continuously listens for events (like HTTP requests) and executes callbacks (functions) when these events occur. This helps Node.js process multiple operations at once without blocking the execution of other operations.

# Non-blocking I/O:
In traditional servers, when an I/O operation (e.g., reading a file or querying a database) occurs, the server waits for the operation to complete before moving on to the next task. However, Node.js uses asynchronous, non-blocking I/O, which means that it doesn’t wait for the I/O operations to finish. Instead, it moves on to handle other tasks and later processes the results when they are available. This increases efficiency and speeds up overall application performance.

# Example: When a Node.js server handles multiple requests, instead of blocking other requests while one is being processed, it continues to process new incoming requests and responds to them as soon as the respective I/O operation finishes.
*/


// 2.) Setting Up Node.js
/* --> Installing Node.js and npm (Node Package Manager)

To get started with Node.js, you need to install both Node.js and npm (which is the Node Package Manager used to manage libraries and dependencies in your project).
# Steps:
i) Download Node.js: Go to the official Node.js website: https://nodejs.org/en. Choose the appropriate version based on your operating system (LTS is recommended for most users).

ii) Install Node.js: Follow the installation steps. This will also install npm automatically, as it comes bundled with Node.js.

iii) Verify the Installation: After installation, open your terminal or command prompt and type:
    
    node -v

# This will display the installed version of Node.js.

iv) Similarly, you can check the installed version of npm:

    npm -v

--> Creating a Simple Node.js Script
# Once Node.js is installed, you can create a simple script to test it.
i) Create a new file (e.g., app.js).

ii) Add the following code to the file:
    
    console.log('Hello, Node.js!');

iii) Run the script with the following command:

    node app.js

This should print "Hello, Node.js!" in your terminal.
*/


// 3.) Understanding the Node.js Runtime
/* The Node.js runtime is an environment that allows JavaScript to be executed on the server side. It consists of the V8 JavaScript engine, which compiles and executes JavaScript, and the libuv library, which provides asynchronous I/O and networking.

--> Key Components of the Node.js Runtime:

i) V8 Engine: The core JavaScript engine that compiles and runs JavaScript.

ii) libuv: A library that handles asynchronous I/O operations, like handling file system requests, networking, etc.

iii) Node.js APIs: Built-in libraries provided by Node.js for working with file systems, HTTP servers, streams, etc.

--> How Node.js Executes JavaScript on the Server
# When you run a Node.js script, the following happens:

i) The V8 engine compiles the JavaScript code into machine code.

ii) Node.js interacts with the operating system and handles I/O operations asynchronously.

iii) It runs on a single thread (main event loop), and asynchronous operations (like I/O) are delegated to the libuv thread pool.

# The event loop processes the callback queue and continuously checks for pending operations. If there are any, it executes their corresponding callbacks.

--> Differences Between Node.js and Traditional Web Servers
#  Feature	            |Traditional Web Servers (e.g., Apache, Nginx)	   |Node.js

1) Concurrency Model	|Multi-threaded	                                   |Single-threaded with event loop
2) Handling of Requests |Each request is handled in a separate thread	   |All requests are handled in a single thread using asynchronous, non-blocking I/O
3) Performance	        |Slower under high load due to thread management   |Faster for high concurrency as it uses non-blocking I/O
4) Ideal Use Case	    |Serving static content, handling simple requests  |Real-time applications (e.g., chat apps, APIs)

--> Conclusion
Node.js allows JavaScript to be used on the server side, making it possible to develop full-stack applications using a single language. Its event-driven, non-blocking I/O model allows it to handle multiple requests simultaneously, making it ideal for building high-performance, scalable applications. By setting up Node.js and running simple scripts, you can quickly begin exploring its capabilities and advantages over traditional web servers.
*/