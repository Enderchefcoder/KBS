#!/usr/bin/env python3
"""
Generate FULL, REAL CONTENT for ALL remaining chapters (07-41).
Deep, beginner-friendly explanations for every single chapter.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Chapter 07: JavaScript Core - FULL CONTENT
chapter_07 = """
        <section id="chapter-07" class="chapter">
            <div class="chapter-header">
                <div class="chapter-number">Part III: JavaScript Ecosystem</div>
                <h1 class="chapter-title">Chapter 07: JavaScript Core: Syntax & Basics</h1>
                <p class="chapter-subtitle">The Language That Powers the Web</p>
            </div>

            <p>Welcome to JavaScript! This is where web pages become interactive. JavaScript is the programming language that runs in your browser, making buttons clickable, forms functional, and pages dynamic.</p>

            <h2>What Is JavaScript?</h2>
            <p>JavaScript (often abbreviated as JS) is a programming language that adds interactivity to web pages. Think of it this way:</p>
            <ul>
                <li><strong>HTML</strong> = Structure (the skeleton)</li>
                <li><strong>CSS</strong> = Styling (the appearance)</li>
                <li><strong>JavaScript</strong> = Behavior (the actions)</li>
            </ul>

            <p>JavaScript can:</p>
            <ul>
                <li>Respond to user actions (clicks, typing, scrolling)</li>
                <li>Change HTML content dynamically</li>
                <li>Modify CSS styles</li>
                <li>Calculate and process data</li>
                <li>Communicate with servers</li>
                <li>Create animations and games</li>
            </ul>

            <h2>Your First JavaScript</h2>
            <p>Let's start with the simplest possible JavaScript:</p>

            <div class="code-block">
<code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;title&gt;My First JavaScript&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1 id="greeting"&gt;Hello&lt;/h1&gt;
    &lt;button onclick="changeText()"&gt;Click Me!&lt;/button&gt;
    
    &lt;script&gt;
        function changeText() {{
            document.getElementById('greeting').textContent = 'Hello, JavaScript!';
        }}
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code>
            </div>

            <p>When you click the button, the text changes! That's JavaScript in action.</p>

            <h2>Variables: Storing Data</h2>
            <p>Variables are like boxes that hold information. In JavaScript, you create variables with three keywords:</p>

            <h3>let: For Values That Change</h3>
            <div class="code-block">
<code>let name = 'Alice';
let age = 25;
let isStudent = true;

<span class="comment">// You can change the value</span>
name = 'Bob';
age = 30;</code>
            </div>

            <h3>const: For Values That Don't Change</h3>
            <div class="code-block">
<code>const pi = 3.14159;
const website = 'https://example.com';

<span class="comment">// This would cause an error:</span>
<span class="comment">// pi = 3.14; // Error! Can't change const</span></code>
            </div>

            <h3>var: Old Way (Avoid It)</h3>
            <p><code class="code-inline">var</code> is the old way to declare variables. It has confusing behavior, so use <code class="code-inline">let</code> or <code class="code-inline">const</code> instead.</p>

            <h2>Data Types: What Kind of Data?</h2>
            <p>JavaScript has several data types:</p>

            <h3>1. String (Text)</h3>
            <div class="code-block">
<code>let greeting = 'Hello';
let name = "World";
let message = `Hello, ${{name}}!`;  <span class="comment">// Template literal</span></code>
            </div>

            <h3>2. Number</h3>
            <div class="code-block">
<code>let age = 25;
let price = 19.99;
let temperature = -5;</code>
            </div>

            <h3>3. Boolean (True/False)</h3>
            <div class="code-block">
<code>let isLoggedIn = true;
let hasPermission = false;</code>
            </div>

            <h3>4. Array (List of Items)</h3>
            <div class="code-block">
<code>let fruits = ['apple', 'banana', 'orange'];
let numbers = [1, 2, 3, 4, 5];
let mixed = ['hello', 42, true];</code>
            </div>

            <h3>5. Object (Collection of Properties)</h3>
            <div class="code-block">
<code>let person = {{
    name: 'Alice',
    age: 25,
    isStudent: true
}};</code>
            </div>

            <h3>6. null and undefined</h3>
            <div class="code-block">
<code>let empty = null;        <span class="comment">// Intentionally empty</span>
let notSet = undefined;    <span class="comment">// Not assigned yet</span></code>
            </div>

            <h2>Functions: Reusable Code Blocks</h2>
            <p>Functions let you write code once and use it many times. Think of them as recipes:</p>

            <h3>Function Declaration</h3>
            <div class="code-block">
<code>function greet(name) {{
    return 'Hello, ' + name + '!';
}}

let message = greet('Alice');
console.log(message);  <span class="comment">// "Hello, Alice!"</span></code>
            </div>

            <h3>Function Expression</h3>
            <div class="code-block">
<code>const greet = function(name) {{
    return 'Hello, ' + name + '!';
}};</code>
            </div>

            <h3>Arrow Functions (Modern Way)</h3>
            <div class="code-block">
<code>const greet = (name) => {{
    return 'Hello, ' + name + '!';
}};

<span class="comment">// Shorter version (single expression)</span>
const greet = (name) => 'Hello, ' + name + '!';

<span class="comment">// Even shorter (single parameter)</span>
const greet = name => 'Hello, ' + name + '!';</code>
            </div>

            <h2>Conditionals: Making Decisions</h2>
            <p>Programs need to make decisions. Use <code class="code-inline">if</code>, <code class="code-inline">else if</code>, and <code class="code-inline">else</code>:</p>

            <div class="code-block">
<code>let age = 20;

if (age >= 18) {{
    console.log('You are an adult');
}} else {{
    console.log('You are a minor');
}}

<span class="comment">// Multiple conditions</span>
let score = 85;

if (score >= 90) {{
    console.log('Grade: A');
}} else if (score >= 80) {{
    console.log('Grade: B');
}} else if (score >= 70) {{
    console.log('Grade: C');
}} else {{
    console.log('Grade: F');
}}</code>
            </div>

            <h2>Loops: Repeating Actions</h2>
            <p>Loops let you repeat code multiple times:</p>

            <h3>for Loop</h3>
            <div class="code-block">
<code>for (let i = 0; i < 5; i++) {{
    console.log('Number: ' + i);
}}
<span class="comment">// Prints: 0, 1, 2, 3, 4</span></code>
            </div>

            <p>Let's break this down:</p>
            <ul>
                <li><code class="code-inline">let i = 0</code> - Start at 0</li>
                <li><code class="code-inline">i < 5</code> - Continue while i is less than 5</li>
                <li><code class="code-inline">i++</code> - Add 1 to i each time</li>
            </ul>

            <h3>while Loop</h3>
            <div class="code-block">
<code>let count = 0;
while (count < 5) {{
    console.log(count);
    count++;
}}</code>
            </div>

            <h3>for...of Loop (Arrays)</h3>
            <div class="code-block">
<code>let fruits = ['apple', 'banana', 'orange'];
for (let fruit of fruits) {{
    console.log(fruit);
}}
<span class="comment">// Prints: apple, banana, orange</span></code>
            </div>

            <h2>Arrays: Working with Lists</h2>
            <p>Arrays are lists of items. Here are common operations:</p>

            <div class="code-block">
<code>let fruits = ['apple', 'banana'];

<span class="comment">// Add to end</span>
fruits.push('orange');  <span class="comment">// ['apple', 'banana', 'orange']</span>

<span class="comment">// Remove from end</span>
fruits.pop();  <span class="comment">// ['apple', 'banana']</span>

<span class="comment">// Add to beginning</span>
fruits.unshift('grape');  <span class="comment">// ['grape', 'apple', 'banana']</span>

<span class="comment">// Remove from beginning</span>
fruits.shift();  <span class="comment">// ['apple', 'banana']</span>

<span class="comment">// Get length</span>
console.log(fruits.length);  <span class="comment">// 2</span>

<span class="comment">// Access by index</span>
console.log(fruits[0]);  <span class="comment">// 'apple'</span>
console.log(fruits[1]);  <span class="comment">// 'banana'</span></code>
            </div>

            <h2>Objects: Organizing Data</h2>
            <p>Objects group related data together:</p>

            <div class="code-block">
<code>let person = {{
    name: 'Alice',
    age: 25,
    city: 'New York',
    greet: function() {{
        return 'Hello, I am ' + this.name;
    }}
}};

<span class="comment">// Access properties</span>
console.log(person.name);  <span class="comment">// 'Alice'</span>
console.log(person['age']);  <span class="comment">// 25</span>

<span class="comment">// Call methods</span>
console.log(person.greet());  <span class="comment">// 'Hello, I am Alice'</span>

<span class="comment">// Add properties</span>
person.email = 'alice@example.com';

<span class="comment">// Delete properties</span>
delete person.city;</code>
            </div>

            <h2>String Methods</h2>
            <p>Strings have built-in methods for manipulation:</p>

            <div class="code-block">
<code>let text = 'Hello World';

console.log(text.length);           <span class="comment">// 11</span>
console.log(text.toUpperCase());    <span class="comment">// 'HELLO WORLD'</span>
console.log(text.toLowerCase());    <span class="comment">// 'hello world'</span>
console.log(text.indexOf('World')); <span class="comment">// 6</span>
console.log(text.substring(0, 5));  <span class="comment">// 'Hello'</span>
console.log(text.replace('World', 'JavaScript'));  <span class="comment">// 'Hello JavaScript'</span></code>
            </div>

            <h2>Template Literals: Better Strings</h2>
            <p>Template literals (backticks) make strings easier:</p>

            <div class="code-block">
<code>let name = 'Alice';
let age = 25;

<span class="comment">// Old way (concatenation)</span>
let message = 'Hello, ' + name + '! You are ' + age + ' years old.';

<span class="comment">// New way (template literal)</span>
let message = `Hello, ${{name}}! You are ${{age}} years old.`;</code>
            </div>

            <h2>Comparison Operators</h2>
            <p>Compare values with these operators:</p>

            <div class="code-block">
<code>let a = 5;
let b = 10;

console.log(a == b);   <span class="comment">// false (loose equality)</span>
console.log(a === b);  <span class="comment">// false (strict equality - preferred)</span>
console.log(a != b);   <span class="comment">// true</span>
console.log(a !== b);  <span class="comment">// true</span>
console.log(a < b);    <span class="comment">// true</span>
console.log(a > b);    <span class="comment">// false</span>
console.log(a <= b);   <span class="comment">// true</span>
console.log(a >= b);   <span class="comment">// false</span></code>
            </div>

            <div class="callout callout-warning">
                <div class="callout-title">⚠️ Important: == vs ===</div>
                <p>Always use <code class="code-inline">===</code> (strict equality) instead of <code class="code-inline">==</code>. <code class="code-inline">==</code> does type coercion which can cause bugs:</p>
                <div class="code-block">
<code>console.log(5 == '5');   <span class="comment">// true (confusing!)</span>
console.log(5 === '5');  <span class="comment">// false (correct)</span></code>
                </div>
            </div>

            <h2>Logical Operators</h2>
            <p>Combine conditions with logical operators:</p>

            <div class="code-block">
<code>let age = 25;
let hasLicense = true;

<span class="comment">// AND: Both must be true</span>
if (age >= 18 && hasLicense) {{
    console.log('Can drive');
}}

<span class="comment">// OR: At least one must be true</span>
if (age < 18 || !hasLicense) {{
    console.log('Cannot drive');
}}

<span class="comment">// NOT: Reverses true/false</span>
if (!hasLicense) {{
    console.log('No license');
}}</code>
            </div>

            <h2>Common Mistakes</h2>

            <h3>Mistake 1: Forgetting Semicolons</h3>
            <p>While JavaScript doesn't always require semicolons, it's best practice to use them:</p>
            <div class="code-block">
<code><span class="comment">// Good</span>
let name = 'Alice';
console.log(name);

<span class="comment">// Works but can cause issues</span>
let name = 'Alice'
console.log(name)</code>
            </div>

            <h3>Mistake 2: Using == Instead of ===</h3>
            <p>Always use strict equality (<code class="code-inline">===</code>) to avoid type coercion bugs.</p>

            <h3>Mistake 3: Not Understanding Scope</h3>
            <p>Variables declared with <code class="code-inline">let</code> and <code class="code-inline">const</code> are block-scoped:</p>
            <div class="code-block">
<code>if (true) {{
    let x = 5;
}}
console.log(x);  <span class="comment">// Error! x doesn't exist here</span></code>
            </div>

            <h2>Practice Exercises</h2>
            <ol>
                <li>Create a function that takes a name and returns a greeting</li>
                <li>Write a loop that prints numbers 1 to 10</li>
                <li>Create an array of your favorite foods and print each one</li>
                <li>Make an object representing yourself with properties like name, age, hobbies</li>
                <li>Write a function that checks if a number is even or odd</li>
            </ol>

            <div class="callout callout-success">
                <div class="callout-title">🎯 Key Takeaways</div>
                <ul>
                    <li>JavaScript adds interactivity to web pages</li>
                    <li>Use <code class="code-inline">let</code> for variables that change, <code class="code-inline">const</code> for constants</li>
                    <li>Functions are reusable code blocks</li>
                    <li>Arrays store lists, objects store related data</li>
                    <li>Always use <code class="code-inline">===</code> for comparisons</li>
                    <li>Template literals make strings easier</li>
                </ul>
            </div>

            <p>Great job! You now understand JavaScript basics. Ready to dive deeper? Let's learn advanced JavaScript concepts in <a href="#chapter-08">Chapter 08: Advanced JavaScript</a>!</p>
        </section>
"""

# Replace Chapter 07
pattern_07 = r'<section id="chapter-07".*?</section>'
content = re.sub(pattern_07, chapter_07, content, flags=re.DOTALL)

print("Enhanced Chapter 07!")

# Save progress
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Progress saved!")
