#!/usr/bin/env python3
"""
Enhance multiple chapters with comprehensive, deep content.
Focuses on adding substantial beginner-friendly explanations.
"""

import re

# Read current file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Enhanced Chapter 05: CSS (expand existing)
enhanced_css = """
        <section id="chapter-05" class="chapter">
            <div class="chapter-header">
                <div class="chapter-number">Part II: Web Fundamentals</div>
                <h1 class="chapter-title">Chapter 05: CSS Essentials: Styling & Layouts</h1>
                <p class="chapter-subtitle">Making Your Web Pages Beautiful</p>
            </div>

            <p>Welcome to CSS! If HTML is the skeleton of a web page, CSS (Cascading Style Sheets) is the skin, clothes, and makeup. It's what makes websites look good.</p>

            <h2>What Is CSS?</h2>
            <p>CSS stands for <strong>Cascading Style Sheets</strong>. Let's break that down:</p>
            <ul>
                <li><strong>Cascading:</strong> Styles can be inherited and overridden (like a waterfall cascading down)</li>
                <li><strong>Style:</strong> How things look (colors, fonts, spacing)</li>
                <li><strong>Sheets:</strong> Files that contain styling rules</li>
            </ul>

            <p>Think of CSS like the styling instructions for a document. HTML says "this is a heading," CSS says "make that heading blue, large, and centered."</p>

            <h2>How CSS Works</h2>
            <p>CSS works by selecting HTML elements and applying styles to them. Here's the basic structure:</p>

            <div class="code-block">
<code><span class="comment">/* This is a CSS comment */</span>
<span class="keyword">selector</span> {{
    <span class="keyword">property</span>: <span class="string">value</span>;
    <span class="keyword">property</span>: <span class="string">value</span>;
}}</code>
            </div>

            <p>Let's understand each part:</p>
            <ul>
                <li><strong>Selector:</strong> Which HTML element(s) to style</li>
                <li><strong>Property:</strong> What aspect to change (like color, size, spacing)</li>
                <li><strong>Value:</strong> What to change it to</li>
            </ul>

            <h2>Your First CSS</h2>
            <p>Let's create a simple example. Create an HTML file and add this CSS:</p>

            <div class="code-block">
<code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;title&gt;My Styled Page&lt;/title&gt;
    &lt;style&gt;
        h1 {{
            color: blue;
            font-size: 48px;
        }}
        
        p {{
            color: #333;
            line-height: 1.6;
        }}
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Hello, World!&lt;/h1&gt;
    &lt;p&gt;This is a styled paragraph.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code>
            </div>

            <p>See the <code class="code-inline">&lt;style&gt;</code> tag in the <code class="code-inline">&lt;head&gt;</code>? That's where we put CSS when it's in the same file as HTML. This is called "internal CSS."</p>

            <h2>Three Ways to Add CSS</h2>
            <p>There are three ways to add CSS to your HTML:</p>

            <h3>1. Inline CSS (In the HTML Element)</h3>
            <div class="code-block">
<code>&lt;p style="color: red; font-size: 20px;"&gt;This is red and large&lt;/p&gt;</code>
            </div>
            <p><strong>When to use:</strong> Rarely. Only for one-off styles. Not recommended for most cases.</p>

            <h3>2. Internal CSS (In the &lt;style&gt; Tag)</h3>
            <div class="code-block">
<code>&lt;head&gt;
    &lt;style&gt;
        p {{ color: red; }}
    &lt;/style&gt;
&lt;/head&gt;</code>
            </div>
            <p><strong>When to use:</strong> Small projects or page-specific styles.</p>

            <h3>3. External CSS (Separate File)</h3>
            <p>Create a file called <code class="code-inline">styles.css</code>:</p>
            <div class="code-block">
<code>p {{
    color: red;
}}</code>
            </div>

            <p>Then link it in your HTML:</p>
            <div class="code-block">
<code>&lt;head&gt;
    &lt;link rel="stylesheet" href="styles.css"&gt;
&lt;/head&gt;</code>
            </div>
            <p><strong>When to use:</strong> Always for larger projects. This is the best practice!</p>

            <h2>CSS Selectors Deep Dive</h2>
            <p>Selectors tell CSS which elements to style. There are many types:</p>

            <h3>Element Selector</h3>
            <p>Selects all elements of that type:</p>
            <div class="code-block">
<code>p {{
    color: blue;
}}</code>
            </div>
            <p>This makes all paragraphs blue.</p>

            <h3>Class Selector</h3>
            <p>Selects elements with a specific class:</p>
            <div class="code-block">
<code><span class="comment">/* CSS */</span>
.highlight {{
    background-color: yellow;
}}</code>
            </div>

            <div class="code-block">
<code>&lt;!-- HTML --&gt;
&lt;p class="highlight"&gt;This is highlighted&lt;/p&gt;</code>
            </div>

            <p>Notice the dot (<code class="code-inline">.</code>) before the class name in CSS? That's how you select classes.</p>

            <h3>ID Selector</h3>
            <p>Selects one specific element with an ID:</p>
            <div class="code-block">
<code><span class="comment">/* CSS */</span>
#main-header {{
    font-size: 48px;
}}</code>
            </div>

            <div class="code-block">
<code>&lt;!-- HTML --&gt;
&lt;h1 id="main-header"&gt;Welcome&lt;/h1&gt;</code>
            </div>

            <p>Notice the hash (<code class="code-inline">#</code>) before the ID? That's how you select IDs. IDs should be unique—only one element per ID.</p>

            <h3>Descendant Selector</h3>
            <p>Selects elements inside other elements:</p>
            <div class="code-block">
<code>div p {{
    color: red;
}}</code>
            </div>
            <p>This selects all paragraphs inside divs.</p>

            <h3>Child Selector</h3>
            <p>Selects direct children only:</p>
            <div class="code-block">
<code>div > p {{
    color: red;
}}</code>
            </div>
            <p>This selects paragraphs that are direct children of divs (not nested deeper).</p>

            <h2>Common CSS Properties</h2>
            <p>Here are the most important CSS properties you'll use constantly:</p>

            <h3>Color Properties</h3>
            <ul>
                <li><code class="code-inline">color</code> - Text color</li>
                <li><code class="code-inline">background-color</code> - Background color</li>
            </ul>

            <h3>Typography Properties</h3>
            <ul>
                <li><code class="code-inline">font-family</code> - Which font to use</li>
                <li><code class="code-inline">font-size</code> - How big the text is</li>
                <li><code class="code-inline">font-weight</code> - Boldness (normal, bold, or numbers 100-900)</li>
                <li><code class="code-inline">line-height</code> - Space between lines</li>
                <li><code class="code-inline">text-align</code> - Alignment (left, center, right, justify)</li>
            </ul>

            <h3>Spacing Properties</h3>
            <ul>
                <li><code class="code-inline">margin</code> - Space outside an element</li>
                <li><code class="code-inline">padding</code> - Space inside an element</li>
            </ul>

            <p>Think of it like a picture frame: <code class="code-inline">padding</code> is the space between the picture and the frame, <code class="code-inline">margin</code> is the space outside the frame.</p>

            <h3>Size Properties</h3>
            <ul>
                <li><code class="code-inline">width</code> - How wide</li>
                <li><code class="code-inline">height</code> - How tall</li>
            </ul>

            <h3>Display Properties</h3>
            <ul>
                <li><code class="code-inline">display</code> - How the element displays (block, inline, flex, grid)</li>
                <li><code class="code-inline">visibility</code> - visible or hidden</li>
            </ul>

            <h2>Understanding the Box Model</h2>
            <p>Every HTML element is a box. Understanding this is crucial for CSS. Each box has:</p>
            <ol>
                <li><strong>Content:</strong> The actual content (text, images, etc.)</li>
                <li><strong>Padding:</strong> Space inside the box, around the content</li>
                <li><strong>Border:</strong> A line around the padding</li>
                <li><strong>Margin:</strong> Space outside the box</li>
            </ol>

            <div class="preview-box">
                <div style="border: 3px solid #2563eb; padding: 20px; margin: 20px; background: #eff6ff;">
                    <p style="margin: 0;">Content (with padding inside, border around, margin outside)</p>
                </div>
            </div>

            <p>When you set <code class="code-inline">width: 200px</code>, that's just the content width. The total width includes padding, border, and margin!</p>

            <h2>CSS Units</h2>
            <p>CSS uses different units for measurements:</p>

            <h3>Absolute Units</h3>
            <ul>
                <li><code class="code-inline">px</code> - Pixels (1px = 1 pixel on screen)</li>
                <li><code class="code-inline">pt</code> - Points (mainly for print)</li>
            </ul>

            <h3>Relative Units</h3>
            <ul>
                <li><code class="code-inline">em</code> - Relative to the font size of the element</li>
                <li><code class="code-inline">rem</code> - Relative to the root element's font size</li>
                <li><code class="code-inline">%</code> - Percentage of the parent element</li>
                <li><code class="code-inline">vh</code> - Viewport height (1vh = 1% of screen height)</li>
                <li><code class="code-inline">vw</code> - Viewport width (1vw = 1% of screen width)</li>
            </ul>

            <p><strong>Pro tip:</strong> Use <code class="code-inline">rem</code> for most sizing—it's predictable and accessible.</p>

            <h2>Colors in CSS</h2>
            <p>There are several ways to specify colors:</p>

            <h3>Named Colors</h3>
            <div class="code-block">
<code>color: red;
color: blue;
color: darkgreen;</code>
            </div>

            <h3>Hexadecimal (Most Common)</h3>
            <div class="code-block">
<code>color: #ff0000; <span class="comment">/* Red */</span>
color: #00ff00; <span class="comment">/* Green */</span>
color: #0000ff; <span class="comment">/* Blue */</span>
color: #333; <span class="comment">/* Dark gray (shorthand) */</span></code>
            </div>

            <p>Hexadecimal colors are written as <code class="code-inline">#RRGGBB</code> where RR is red, GG is green, BB is blue. Each is a value from 00 (none) to FF (maximum).</p>

            <h3>RGB</h3>
            <div class="code-block">
<code>color: rgb(255, 0, 0); <span class="comment">/* Red */</span>
color: rgba(255, 0, 0, 0.5); <span class="comment">/* Red with 50% opacity */</span></code>
            </div>

            <h3>HSL</h3>
            <div class="code-block">
<code>color: hsl(0, 100%, 50%); <span class="comment">/* Red */</span>
color: hsla(0, 100%, 50%, 0.5); <span class="comment">/* Red with transparency */</span></code>
            </div>

            <h2>CSS Layout: Flexbox</h2>
            <p>Flexbox is a powerful layout system. It makes it easy to align and distribute space among items.</p>

            <p>To use flexbox, set <code class="code-inline">display: flex</code> on a container:</p>

            <div class="code-block">
<code>.container {{
    display: flex;
    justify-content: center; <span class="comment">/* Horizontal alignment */</span>
    align-items: center; <span class="comment">/* Vertical alignment */</span>
    gap: 20px; <span class="comment">/* Space between items */</span>
}}</code>
            </div>

            <p>Common flexbox properties:</p>
            <ul>
                <li><code class="code-inline">justify-content</code> - Aligns items along the main axis (horizontal by default)</li>
                <li><code class="code-inline">align-items</code> - Aligns items along the cross axis (vertical by default)</li>
                <li><code class="code-inline">flex-direction</code> - row (default) or column</li>
                <li><code class="code-inline">flex-wrap</code> - Whether items wrap to new lines</li>
                <li><code class="code-inline">gap</code> - Space between items</li>
            </ul>

            <h2>CSS Layout: Grid</h2>
            <p>CSS Grid is perfect for two-dimensional layouts (rows and columns).</p>

            <div class="code-block">
<code>.container {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr; <span class="comment">/* 3 equal columns */</span>
    grid-template-rows: auto;
    gap: 20px;
}}</code>
            </div>

            <p><code class="code-inline">fr</code> stands for "fraction"—it divides available space proportionally.</p>

            <h2>Responsive Design Basics</h2>
            <p>Responsive design means your website looks good on all screen sizes. Use media queries:</p>

            <div class="code-block">
<code><span class="comment">/* Default styles */</span>
.container {{
    width: 100%;
}}

<span class="comment">/* Styles for screens wider than 768px */</span>
@media (min-width: 768px) {{
    .container {{
        width: 750px;
        margin: 0 auto;
    }}
}}</code>
            </div>

            <p>This is a "mobile-first" approach—design for mobile, then enhance for larger screens.</p>

            <h2>CSS Best Practices</h2>
            <ul>
                <li>Use external stylesheets for larger projects</li>
                <li>Use semantic class names (<code class="code-inline">.button-primary</code> not <code class="code-inline">.blue-thing</code>)</li>
                <li>Keep specificity low (avoid too many nested selectors)</li>
                <li>Use variables (CSS custom properties) for colors and sizes</li>
                <li>Comment your code</li>
            </ul>

            <div class="callout callout-success">
                <div class="callout-title">🎯 Key Takeaways</div>
                <ul>
                    <li>CSS controls how HTML elements look</li>
                    <li>Use selectors to target elements</li>
                    <li>Understand the box model (content, padding, border, margin)</li>
                    <li>Flexbox and Grid are powerful layout tools</li>
                    <li>Always design responsively</li>
                </ul>
            </div>

            <p>Ready for advanced CSS? Let's learn animations and more in <a href="#chapter-06">Chapter 06: Advanced CSS</a>!</p>
        </section>
"""

# Replace Chapter 05
pattern_05 = r'<section id="chapter-05".*?</section>'
content = re.sub(pattern_05, enhanced_css, content, flags=re.DOTALL)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Enhanced Chapter 05 with comprehensive CSS content!")
