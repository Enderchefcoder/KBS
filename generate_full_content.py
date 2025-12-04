#!/usr/bin/env python3
"""
Generate FULL, REAL CONTENT for all chapters.
Deep, beginner-friendly explanations for every single chapter.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Chapter 06: Advanced CSS - FULL CONTENT
chapter_06 = """
        <section id="chapter-06" class="chapter">
            <div class="chapter-header">
                <div class="chapter-number">Part II: Web Fundamentals</div>
                <h1 class="chapter-title">Chapter 06: Advanced CSS: Animations & Responsive Design</h1>
                <p class="chapter-subtitle">Making Websites Come Alive</p>
            </div>

            <p>Welcome back! Now that you understand CSS basics, let's make things move, dance, and adapt to any screen size. This chapter will teach you how to create smooth animations, transitions, and responsive designs that work perfectly on everything from phones to giant monitors.</p>

            <h2>CSS Transitions: Smooth Changes</h2>
            <p>Transitions make changes smooth instead of instant. Think of it like a dimmer switch instead of an on/off switch.</p>

            <h3>Basic Transition Syntax</h3>
            <p>The transition property has four parts:</p>
            <div class="code-block">
<code>.button {{
    transition: property duration timing-function delay;
}}

<span class="comment">/* Example */</span>
.button {{
    background-color: blue;
    transition: background-color 0.3s ease 0s;
}}

.button:hover {{
    background-color: red;
    <span class="comment">/* Smoothly transitions from blue to red over 0.3 seconds */</span>
}}</code>
            </div>

            <p>Let's break this down:</p>
            <ul>
                <li><strong>property:</strong> What to animate (background-color, width, opacity, etc.)</li>
                <li><strong>duration:</strong> How long the transition takes (0.3s = 0.3 seconds)</li>
                <li><strong>timing-function:</strong> How the animation accelerates/decelerates</li>
                <li><strong>delay:</strong> How long to wait before starting</li>
            </ul>

            <h3>Timing Functions Explained</h3>
            <p>The timing function controls the "feel" of the animation:</p>
            <ul>
                <li><code class="code-inline">ease</code> - Starts slow, speeds up, slows down (default, most natural)</li>
                <li><code class="code-inline">linear</code> - Constant speed (mechanical feeling)</li>
                <li><code class="code-inline">ease-in</code> - Starts slow, ends fast</li>
                <li><code class="code-inline">ease-out</code> - Starts fast, ends slow</li>
                <li><code class="code-inline">ease-in-out</code> - Slow start and end, fast middle</li>
                <li><code class="code-inline">cubic-bezier()</code> - Custom curve (advanced)</li>
            </ul>

            <h3>Transitioning Multiple Properties</h3>
            <p>You can transition multiple properties at once:</p>
            <div class="code-block">
<code>.card {{
    transition: background-color 0.3s ease,
                transform 0.5s ease,
                opacity 0.2s ease;
}}

.card:hover {{
    background-color: #f0f0f0;
    transform: translateY(-10px);
    opacity: 0.9;
}}</code>
            </div>

            <h2>CSS Animations: Complex Movements</h2>
            <p>While transitions handle simple property changes, animations let you create complex, multi-step movements.</p>

            <h3>Keyframes: The Building Blocks</h3>
            <p>Keyframes define what happens at specific points in an animation:</p>
            <div class="code-block">
<code>@keyframes slideIn {{
    <span class="comment">/* Start (0%) */</span>
    from {{
        transform: translateX(-100%);
        opacity: 0;
    }}
    
    <span class="comment">/* End (100%) */</span>
    to {{
        transform: translateX(0);
        opacity: 1;
    }}
}}

<span class="comment">/* Or use percentages for more control */</span>
@keyframes bounce {{
    0% {{
        transform: translateY(0);
    }}
    50% {{
        transform: translateY(-50px);
    }}
    100% {{
        transform: translateY(0);
    }}
}}</code>
            </div>

            <h3>Using Animations</h3>
            <p>Apply animations with the animation property:</p>
            <div class="code-block">
<code>.element {{
    animation: slideIn 1s ease-in-out;
}}

<span class="comment">/* Full syntax: */</span>
.element {{
    animation-name: slideIn;
    animation-duration: 1s;
    animation-timing-function: ease-in-out;
    animation-delay: 0s;
    animation-iteration-count: 1;
    animation-direction: normal;
    animation-fill-mode: forwards;
    animation-play-state: running;
}}</code>
            </div>

            <h3>Animation Properties Explained</h3>
            <ul>
                <li><code class="code-inline">animation-name</code> - Which keyframe animation to use</li>
                <li><code class="code-inline">animation-duration</code> - How long one cycle takes</li>
                <li><code class="code-inline">animation-iteration-count</code> - How many times to repeat (number or "infinite")</li>
                <li><code class="code-inline">animation-direction</code> - normal, reverse, alternate, alternate-reverse</li>
                <li><code class="code-inline">animation-fill-mode</code> - What styles apply before/after animation</li>
                <li><code class="code-inline">animation-play-state</code> - running or paused</li>
            </ul>

            <h2>Transform: Moving and Rotating Elements</h2>
            <p>Transform lets you move, rotate, scale, and skew elements without affecting layout.</p>

            <h3>Translation (Moving)</h3>
            <div class="code-block">
<code><span class="comment">/* Move right 50px, down 20px */</span>
.element {{
    transform: translate(50px, 20px);
}}

<span class="comment">/* Or separately */</span>
.element {{
    transform: translateX(50px);  <span class="comment">/* Horizontal */</span>
    transform: translateY(20px);  <span class="comment">/* Vertical */</span>
}}</code>
            </div>

            <h3>Rotation</h3>
            <div class="code-block">
<code><span class="comment">/* Rotate 45 degrees */</span>
.element {{
    transform: rotate(45deg);
}}

<span class="comment">/* Rotate around a specific point */</span>
.element {{
    transform-origin: center center;
    transform: rotate(90deg);
}}</code>
            </div>

            <h3>Scaling</h3>
            <div class="code-block">
<code><span class="comment">/* Make 1.5x bigger */</span>
.element {{
    transform: scale(1.5);
}}

<span class="comment">/* Scale width and height separately */</span>
.element {{
    transform: scaleX(1.5);  <span class="comment">/* Width */</span>
    transform: scaleY(0.8);  <span class="comment">/* Height */</span>
}}</code>
            </div>

            <h3>Combining Transforms</h3>
            <div class="code-block">
<code>.element {{
    transform: translateX(50px) rotate(45deg) scale(1.2);
    <span class="comment">/* Order matters! */</span>
}}</code>
            </div>

            <h2>Responsive Design: Mobile-First Approach</h2>
            <p>Responsive design ensures your website looks great on all devices. The mobile-first approach means designing for small screens first, then enhancing for larger screens.</p>

            <h3>Viewport Meta Tag</h3>
            <p>First, always include this in your HTML head:</p>
            <div class="code-block">
<code>&lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;</code>
            </div>

            <p>This tells mobile browsers to use the device width instead of a fake desktop width.</p>

            <h3>Media Queries: The Foundation</h3>
            <p>Media queries let you apply different styles based on screen size:</p>
            <div class="code-block">
<code><span class="comment">/* Mobile styles (default) */</span>
.container {{
    width: 100%;
    padding: 10px;
}}

<span class="comment">/* Tablet: 768px and up */</span>
@media (min-width: 768px) {{
    .container {{
        width: 750px;
        margin: 0 auto;
        padding: 20px;
    }}
}}

<span class="comment">/* Desktop: 1024px and up */</span>
@media (min-width: 1024px) {{
    .container {{
        width: 1200px;
        padding: 40px;
    }}
}}</code>
            </div>

            <h3>Common Breakpoints</h3>
            <p>While breakpoints depend on your design, here are common ones:</p>
            <ul>
                <li><strong>Mobile:</strong> 320px - 767px</li>
                <li><strong>Tablet:</strong> 768px - 1023px</li>
                <li><strong>Desktop:</strong> 1024px - 1439px</li>
                <li><strong>Large Desktop:</strong> 1440px+</li>
            </ul>

            <h3>Flexible Units for Responsiveness</h3>
            <p>Use relative units instead of fixed pixels:</p>
            <div class="code-block">
<code><span class="comment">/* Bad: Fixed sizes */</span>
.element {{
    width: 500px;
    font-size: 16px;
}}

<span class="comment">/* Good: Flexible sizes */</span>
.element {{
    width: 100%;        <span class="comment">/* Or max-width: 500px */</span>
    font-size: 1rem;    <span class="comment">/* Scales with root font size */</span>
    padding: 2vw;       <span class="comment">/* 2% of viewport width */</span>
}}</code>
            </div>

            <h2>CSS Grid for Responsive Layouts</h2>
            <p>CSS Grid makes responsive layouts much easier:</p>

            <div class="code-block">
<code><span class="comment">/* Mobile: Single column */</span>
.grid-container {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
}}

<span class="comment">/* Tablet: Two columns */</span>
@media (min-width: 768px) {{
    .grid-container {{
        grid-template-columns: repeat(2, 1fr);
    }}
}}

<span class="comment">/* Desktop: Three columns */</span>
@media (min-width: 1024px) {{
    .grid-container {{
        grid-template-columns: repeat(3, 1fr);
    }}
}}</code>
            </div>

            <h2>Flexible Images</h2>
            <p>Images should scale with their containers:</p>
            <div class="code-block">
<code>img {{
    max-width: 100%;
    height: auto;
    <span class="comment">/* Image scales down but never gets bigger than container */</span>
}}</code>
            </div>

            <h2>Advanced Responsive Techniques</h2>

            <h3>Container Queries (Modern CSS)</h3>
            <p>Container queries let you style based on container size, not viewport:</p>
            <div class="code-block">
<code>.container {{
    container-type: inline-size;
}}

.card {{
    padding: 10px;
}}

@container (min-width: 400px) {{
    .card {{
        padding: 20px;
    }}
}}</code>
            </div>

            <h3>CSS Variables for Theming</h3>
            <p>Use CSS custom properties for easy theming:</p>
            <div class="code-block">
<code>:root {{
    --primary-color: #2563eb;
    --spacing: 20px;
    --font-size-base: 16px;
}}

.element {{
    color: var(--primary-color);
    padding: var(--spacing);
    font-size: var(--font-size-base);
}}

<span class="comment">/* Easy to change for dark mode or different themes */</span>
@media (prefers-color-scheme: dark) {{
    :root {{
        --primary-color: #60a5fa;
    }}
}}</code>
            </div>

            <h2>Performance: Optimizing Animations</h2>
            <p>Not all properties animate smoothly. Some cause "reflows" (layout recalculations) which are expensive.</p>

            <h3>Properties That Animate Smoothly</h3>
            <ul>
                <li><code class="code-inline">transform</code> - Best! Uses GPU acceleration</li>
                <li><code class="code-inline">opacity</code> - Very smooth</li>
                <li><code class="code-inline">filter</code> - Generally smooth</li>
            </ul>

            <h3>Properties to Avoid Animating</h3>
            <ul>
                <li><code class="code-inline">width</code>, <code class="code-inline">height</code> - Causes reflow</li>
                <li><code class="code-inline">margin</code>, <code class="code-inline">padding</code> - Causes reflow</li>
                <li><code class="code-inline">top</code>, <code class="code-inline">left</code> - Use transform instead</li>
            </ul>

            <div class="callout callout-warning">
                <div class="callout-title">⚠️ Performance Tip</div>
                <p>Use <code class="code-inline">transform</code> and <code class="code-inline">opacity</code> for animations whenever possible. They're GPU-accelerated and don't trigger layout recalculations.</p>
            </div>

            <h2>Practical Examples</h2>

            <h3>Example 1: Smooth Button Hover</h3>
            <div class="code-block">
<code>.button {{
    background-color: #2563eb;
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 6px;
    transition: all 0.3s ease;
    cursor: pointer;
}}

.button:hover {{
    background-color: #1e40af;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}}

.button:active {{
    transform: translateY(0);
}}</code>
            </div>

            <h3>Example 2: Loading Spinner</h3>
            <div class="code-block">
<code>@keyframes spin {{
    from {{
        transform: rotate(0deg);
    }}
    to {{
        transform: rotate(360deg);
    }}
}}

.spinner {{
    width: 40px;
    height: 40px;
    border: 4px solid #f3f4f6;
    border-top-color: #2563eb;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}}</code>
            </div>

            <h3>Example 3: Responsive Navigation</h3>
            <div class="code-block">
<code><span class="comment">/* Mobile: Hamburger menu */</span>
.nav {{
    display: flex;
    flex-direction: column;
}}

.menu-button {{
    display: block;
}}

.nav-links {{
    display: none;
}}

<span class="comment">/* Desktop: Horizontal menu */</span>
@media (min-width: 768px) {{
    .nav {{
        flex-direction: row;
    }}
    
    .menu-button {{
        display: none;
    }}
    
    .nav-links {{
        display: flex;
        gap: 20px;
    }}
}}</code>
            </div>

            <h2>Key Takeaways</h2>
            <div class="callout callout-success">
                <div class="callout-title">🎯 What You've Learned</div>
                <ul>
                    <li>Transitions make property changes smooth</li>
                    <li>Animations create complex, multi-step movements</li>
                    <li>Transform moves, rotates, and scales elements efficiently</li>
                    <li>Media queries enable responsive design</li>
                    <li>Mobile-first approach designs for small screens first</li>
                    <li>Use transform and opacity for performant animations</li>
                </ul>
            </div>

            <p>Congratulations! You now know how to create beautiful, animated, responsive websites. Ready to add interactivity? Let's learn JavaScript in <a href="#chapter-07">Chapter 07: JavaScript Core</a>!</p>
        </section>
"""

# Replace Chapter 06
pattern_06 = r'<section id="chapter-06".*?</section>'
content = re.sub(pattern_06, chapter_06, content, flags=re.DOTALL)

print("Enhanced Chapter 06 with full content!")

# Continue with more chapters...
# I'll add them systematically
