#!/usr/bin/env python3
"""
Replace Chapter 24 with comprehensive, deep content about AI Stack,
Transformers, Layers, Neural Networks - explained like to a middle schooler.
"""

comprehensive_chapter_24 = """
        <section id="chapter-24" class="chapter">
            <div class="chapter-header">
                <div class="chapter-number">Part V: Python & Artificial Intelligence</div>
                <h1 class="chapter-title">Chapter 24: The AI Stack: Torch, TensorFlow, & Transformers</h1>
                <p class="chapter-subtitle">Understanding How AI Actually Works</p>
            </div>

            <p>Welcome to one of the most exciting chapters in this book! By the end of this chapter, you'll understand how ChatGPT, image generators, and other AI systems actually work. We're going to go <em>deep</em>—explaining everything as if you've never heard of AI before.</p>

            <h2>What Is Artificial Intelligence, Really?</h2>
            <p>Before we dive into Transformers and neural networks, let's start with the absolute basics: What is artificial intelligence?</p>

            <p>Think of AI like teaching a computer to recognize patterns. Imagine you're teaching a child to recognize cats. You show them thousands of pictures of cats, and eventually, they learn what makes a cat a cat. AI does something similar—but with math instead of human intuition.</p>

            <p>Here's the key insight: <strong>AI isn't magic. It's math.</strong> Specifically, it's a lot of multiplication, addition, and finding patterns in numbers. Once you understand that, everything else makes sense.</p>

            <h2>Understanding Neural Networks: The Foundation</h2>
            <p>Before we can understand Transformers (the technology behind ChatGPT), we need to understand neural networks. And before we understand neural networks, we need to understand what a "neuron" is.</p>

            <h3>What Is a Neuron? (In Your Brain)</h3>
            <p>Your brain has billions of cells called neurons. Each neuron:</p>
            <ol>
                <li>Receives signals from other neurons</li>
                <li>Decides whether those signals are strong enough</li>
                <li>Sends a signal to other neurons if they are</li>
            </ol>

            <p>Think of it like a light switch with a dimmer. If enough electricity flows in, the switch turns on and sends electricity out. But it's not just on or off—it can be partially on, depending on how much electricity comes in.</p>

            <h3>What Is an Artificial Neuron? (In a Computer)</h3>
            <p>An artificial neuron is a computer program that mimics what a real neuron does:</p>
            <ol>
                <li>It receives numbers (instead of electrical signals)</li>
                <li>It multiplies each number by a "weight" (like turning a dial)</li>
                <li>It adds all those weighted numbers together</li>
                <li>It applies an "activation function" (decides whether to "fire")</li>
                <li>It sends the result to other neurons</li>
            </ol>

            <p>Let's see this in action with the simplest possible example:</p>

            <div class="code-block">
<code><span class="comment"># A super simple artificial neuron</span>
<span class="keyword">def</span> <span class="function">simple_neuron</span>(inputs, weights):
    <span class="comment"># Step 1: Multiply each input by its weight</span>
    weighted_sum = <span class="number">0</span>
    <span class="keyword">for</span> i <span class="keyword">in</span> <span class="function">range</span>(<span class="function">len</span>(inputs)):
        weighted_sum += inputs[i] * weights[i]
    
    <span class="comment"># Step 2: Apply activation function (simple: if sum > 0, return 1, else 0)</span>
    <span class="keyword">if</span> weighted_sum > <span class="number">0</span>:
        <span class="keyword">return</span> <span class="number">1</span>
    <span class="keyword">else</span>:
        <span class="keyword">return</span> <span class="number">0</span>

<span class="comment"># Example: Is this a cat picture?</span>
<span class="comment"># Inputs: [has_fur=1, has_whiskers=1, has_tail=1]</span>
<span class="comment"># Weights: [0.5, 0.8, 0.3] (whiskers are most important)</span>
inputs = [<span class="number">1</span>, <span class="number">1</span>, <span class="number">1</span>]
weights = [<span class="number">0.5</span>, <span class="number">0.8</span>, <span class="number">0.3</span>]
result = <span class="function">simple_neuron</span>(inputs, weights)
<span class="function">print</span>(result) <span class="comment"># Output: 1 (yes, it's a cat!)</span></code>
            </div>

            <p>This neuron takes three inputs (does it have fur? whiskers? a tail?), multiplies each by its importance (weight), adds them up, and decides: "Yes, this is probably a cat!"</p>

            <p>But one neuron can't do much. You need many neurons working together. That's where layers come in.</p>

            <h2>What Is a Layer? (Explained Deeply)</h2>
            <p>This is crucial: <strong>What is a layer?</strong> Let me explain this as if you're in middle school.</p>

            <h3>Layer = A Group of Neurons Working Together</h3>
            <p>Imagine you're organizing a school project. You have different groups (layers), and each group has a specific job:</p>
            <ul>
                <li><strong>Input Layer:</strong> The first group receives the raw information (like a picture's pixels)</li>
                <li><strong>Hidden Layers:</strong> Middle groups that process the information step by step</li>
                <li><strong>Output Layer:</strong> The final group that gives you the answer</li>
            </ul>

            <p>Here's a visual way to think about it:</p>

            <div class="preview-box">
                <div style="text-align: center; padding: 20px;">
                    <div style="display: inline-block; margin: 10px; padding: 15px; background: #e0f2fe; border-radius: 8px;">
                        <strong>Input Layer</strong><br>
                        <small>3 neurons</small><br>
                        <small>Receives: Picture pixels</small>
                    </div>
                    <span style="font-size: 24px;">→</span>
                    <div style="display: inline-block; margin: 10px; padding: 15px; background: #fef3c7; border-radius: 8px;">
                        <strong>Hidden Layer 1</strong><br>
                        <small>5 neurons</small><br>
                        <small>Finds: Edges, shapes</small>
                    </div>
                    <span style="font-size: 24px;">→</span>
                    <div style="display: inline-block; margin: 10px; padding: 15px; background: #fef3c7; border-radius: 8px;">
                        <strong>Hidden Layer 2</strong><br>
                        <small>4 neurons</small><br>
                        <small>Finds: Patterns, features</small>
                    </div>
                    <span style="font-size: 24px;">→</span>
                    <div style="display: inline-block; margin: 10px; padding: 15px; background: #d1fae5; border-radius: 8px;">
                        <strong>Output Layer</strong><br>
                        <small>2 neurons</small><br>
                        <small>Answer: Cat or Dog?</small>
                    </div>
                </div>
            </div>

            <p>Each layer takes the output from the previous layer, processes it, and sends it to the next layer. It's like a factory assembly line, where each station (layer) does a specific job.</p>

            <h3>Why Multiple Layers?</h3>
            <p>Why not just one big layer? Because each layer learns to recognize different levels of complexity:</p>
            <ul>
                <li><strong>Layer 1:</strong> Recognizes simple things (edges, corners, colors)</li>
                <li><strong>Layer 2:</strong> Recognizes combinations (circles, squares, lines)</li>
                <li><strong>Layer 3:</strong> Recognizes complex patterns (eyes, noses, ears)</li>
                <li><strong>Layer 4:</strong> Recognizes complete objects (faces, animals)</li>
            </ul>

            <p>It's like learning to read: First you learn letters, then words, then sentences, then paragraphs. Each layer builds on the previous one.</p>

            <h3>How Many Neurons in a Layer?</h3>
            <p>This is where it gets interesting. A layer can have any number of neurons:</p>
            <ul>
                <li><strong>Small layer:</strong> 10-100 neurons (for simple tasks)</li>
                <li><strong>Medium layer:</strong> 100-1000 neurons (for moderate tasks)</li>
                <li><strong>Large layer:</strong> 1000-100,000 neurons (for complex tasks)</li>
                <li><strong>Huge layer:</strong> 100,000+ neurons (for very complex tasks like GPT)</li>
            </ul>

            <p>More neurons = more capacity to learn complex patterns, but also more computation needed.</p>

            <h3>How Layers Connect</h3>
            <p>Here's the crucial part: <strong>Every neuron in one layer connects to every neuron in the next layer.</strong></p>

            <p>If Layer 1 has 3 neurons and Layer 2 has 5 neurons, that's 3 × 5 = 15 connections! Each connection has a weight (a number that determines how important that connection is).</p>

            <p>Let's visualize this:</p>

            <div class="code-block">
<code><span class="comment"># Simplified representation of layers</span>
<span class="comment"># Layer 1: 3 neurons</span>
layer1 = [neuron1, neuron2, neuron3]

<span class="comment"># Layer 2: 5 neurons</span>
<span class="comment"># Each neuron in layer2 receives input from ALL neurons in layer1</span>
layer2 = [
    neuron(weights=[w1_1, w1_2, w1_3]), <span class="comment"># Connected to all 3 neurons in layer1</span>
    neuron(weights=[w2_1, w2_2, w2_3]),
    neuron(weights=[w3_1, w3_2, w3_3]),
    neuron(weights=[w4_1, w4_2, w4_3]),
    neuron(weights=[w5_1, w5_2, w5_3])
]</code>
            </div>

            <p>This "fully connected" structure is what makes neural networks powerful—every neuron can influence every other neuron in the next layer.</p>

            <h2>What Is "Training"? (The Learning Process)</h2>
            <p>Now here's the magic: How does a neural network learn? Through a process called "training."</p>

            <h3>Training = Teaching by Example</h3>
            <p>Imagine teaching a child to recognize animals:</p>
            <ol>
                <li>You show them a picture: "This is a cat"</li>
                <li>They guess: "Dog?"</li>
                <li>You correct them: "No, it's a cat. Look at the whiskers."</li>
                <li>They adjust their understanding</li>
                <li>Repeat thousands of times</li>
            </ol>

            <p>Neural networks learn the same way:</p>
            <ol>
                <li><strong>Forward Pass:</strong> Show the network an image, it makes a prediction</li>
                <li><strong>Calculate Error:</strong> Compare prediction to correct answer</li>
                <li><strong>Backward Pass (Backpropagation):</strong> Go backwards through the network, adjusting weights to reduce error</li>
                <li><strong>Repeat:</strong> Do this millions of times with millions of examples</li>
            </ol>

            <p>The weights start random, but through training, they adjust to recognize patterns. It's like tuning a radio—you keep adjusting until you get a clear signal.</p>

            <h2>Understanding Transformers (The Big One)</h2>
            <p>Now we're ready for Transformers! This is the technology behind ChatGPT, GPT-4, and most modern AI language models.</p>

            <h3>What Is a Transformer? (Simple Explanation)</h3>
            <p>A Transformer is a specific type of neural network architecture. "Architecture" just means "how the neurons are organized."</p>

            <p>Think of it like different building designs:</p>
            <ul>
                <li>A regular house (traditional neural network) has rooms connected in a simple way</li>
                <li>A Transformer (like a skyscraper) has a special design optimized for processing sequences (like sentences)</li>
            </ul>

            <h3>Why Are They Called "Transformers"?</h3>
            <p>They're called Transformers because they <em>transform</em> sequences of data (like words in a sentence) into a format that the network can understand and process.</p>

            <p>Think of it like translating between languages: You take English words, transform them into a mathematical representation, process them, then transform them back into English (but better!).</p>

            <h3>The Key Innovation: Attention</h3>
            <p>Here's what makes Transformers special: <strong>Attention Mechanism</strong>.</p>

            <p>Imagine you're reading this sentence: "The cat sat on the mat." When you read "sat," your brain automatically connects it to "cat" (what sat?) and "mat" (where did it sit?). You're paying <em>attention</em> to the relevant words.</p>

            <p>Transformers do the same thing! When processing a word, they look at all other words in the sentence and decide which ones are most relevant. This is called "self-attention."</p>

            <h3>How Transformers Work (Step by Step)</h3>
            <p>Let's break down exactly how a Transformer processes text:</p>

            <h4>Step 1: Tokenization</h4>
            <p>First, the sentence is broken into "tokens" (usually words or parts of words):</p>
            <div class="code-block">
<code><span class="comment"># "Hello world" becomes:</span>
tokens = [<span class="string">"Hello"</span>, <span class="string">"world"</span>]</code>
            </div>

            <h4>Step 2: Embedding</h4>
            <p>Each token is converted into a vector (a list of numbers). Words with similar meanings get similar vectors:</p>
            <div class="code-block">
<code><span class="comment"># "cat" might become:</span>
cat_vector = [<span class="number">0.2</span>, <span class="number">0.8</span>, <span class="number">-0.1</span>, <span class="number">0.5</span>, ...] <span class="comment"># 768 numbers!</span>

<span class="comment"># "dog" (similar to cat) might be:</span>
dog_vector = [<span class="number">0.3</span>, <span class="number">0.7</span>, <span class="number">-0.2</span>, <span class="number">0.4</span>, ...] <span class="comment"># Similar numbers!</span>

<span class="comment"># "airplane" (very different) might be:</span>
airplane_vector = [<span class="number">-0.8</span>, <span class="number">0.1</span>, <span class="number">0.9</span>, <span class="number">-0.3</span>, ...] <span class="comment"># Very different!</span></code>
            </div>

            <h4>Step 3: Position Encoding</h4>
            <p>Since Transformers process all words at once (unlike older models that went word-by-word), they need to know word order. Position encoding adds information about where each word is:</p>
            <div class="code-block">
<code><span class="comment"># "Hello" is position 0, "world" is position 1</span>
<span class="comment"># This information is added to the embeddings</span></code>
            </div>

            <h4>Step 4: Self-Attention (The Magic)</h4>
            <p>This is where Transformers shine. For each word, the model calculates how much attention to pay to every other word:</p>

            <div class="preview-box">
                <div class="preview-title">Example: "The cat sat on the mat"</div>
                <p>When processing "sat":</p>
                <ul>
                    <li>Pays 40% attention to "cat" (what sat?)</li>
                    <li>Pays 30% attention to "mat" (where?)</li>
                    <li>Pays 20% attention to "on" (preposition)</li>
                    <li>Pays 10% attention to "The" (article)</li>
                </ul>
            </div>

            <p>This attention is learned during training—the model figures out which words are important for understanding each word.</p>

            <h4>Step 5: Feed-Forward Networks</h4>
            <p>After attention, the information goes through a feed-forward neural network (regular layers) that processes it further.</p>

            <h4>Step 6: Repeat (Multiple Layers)</h4>
            <p>Steps 4-5 repeat multiple times (GPT-3 has 96 layers!). Each layer refines the understanding.</p>

            <h4>Step 7: Output</h4>
            <p>Finally, the processed information is converted back into probabilities for the next word.</p>

            <h3>Why Transformers Are So Powerful</h3>
            <p>Transformers are powerful because:</p>
            <ol>
                <li><strong>Parallel Processing:</strong> They can process all words simultaneously (unlike older sequential models)</li>
                <li><strong>Long-Range Dependencies:</strong> They can connect words that are far apart in a sentence</li>
                <li><strong>Scalability:</strong> They scale well—bigger models = better performance</li>
                <li><strong>Transfer Learning:</strong> Once trained on lots of text, they can be fine-tuned for specific tasks</li>
            </ol>

            <h2>PyTorch vs TensorFlow: The Two Main Frameworks</h2>
            <p>Now that you understand neural networks and Transformers, let's talk about the tools used to build them.</p>

            <h3>What Is a Framework?</h3>
            <p>A framework is like a toolkit. Instead of building everything from scratch, you use pre-built tools. PyTorch and TensorFlow are frameworks for building neural networks.</p>

            <h3>PyTorch: The Researcher's Choice</h3>
            <p>PyTorch is like a flexible workshop where you can build anything:</p>
            <ul>
                <li><strong>Pros:</strong> Easy to debug, Pythonic, great for research</li>
                <li><strong>Cons:</strong> Slightly slower for production</li>
                <li><strong>Used by:</strong> Most research labs, Meta (Facebook)</li>
            </ul>

            <h3>TensorFlow: The Production Choice</h3>
            <p>TensorFlow is like an industrial factory—optimized for production:</p>
            <ul>
                <li><strong>Pros:</strong> Great for deployment, supports many languages</li>
                <li><strong>Cons:</strong> More complex, steeper learning curve</li>
                <li><strong>Used by:</strong> Google, many production systems</li>
            </ul>

            <h3>Which Should You Learn?</h3>
            <p>Both! But start with PyTorch—it's easier to learn and understand. Once you know one, learning the other is much easier.</p>

            <h2>Hugging Face Transformers: Using Pre-Built Models</h2>
            <p>You don't have to build Transformers from scratch! Hugging Face provides pre-trained models you can use:</p>

            <div class="code-block">
<code><span class="keyword">from</span> transformers <span class="keyword">import</span> pipeline

<span class="comment"># Use a pre-trained model for text generation</span>
generator = pipeline(<span class="string">"text-generation"</span>, model=<span class="string">"gpt2"</span>)
result = generator(<span class="string">"The future of AI is"</span>, max_length=<span class="number">50</span>)
<span class="function">print</span>(result)</code>
            </div>

            <p>This is like using a pre-built car instead of building one from scratch. You can still customize it, but you don't start from zero.</p>

            <h2>Real-World Applications</h2>
            <p>Where are Transformers actually used?</p>
            <ul>
                <li><strong>ChatGPT:</strong> Conversational AI</li>
                <li><strong>Code Completion:</strong> GitHub Copilot, Cursor</li>
                <li><strong>Translation:</strong> Google Translate</li>
                <li><strong>Image Generation:</strong> DALL-E, Midjourney (use similar architectures)</li>
                <li><strong>Summarization:</strong> Summarizing long documents</li>
            </ul>

            <h2>Key Takeaways</h2>
            <div class="callout callout-success">
                <div class="callout-title">🎯 What You've Learned</div>
                <ul>
                    <li>Neural networks are made of neurons (simple math functions) organized in layers</li>
                    <li>Layers process information step by step, each building on the previous</li>
                    <li>Training adjusts weights through millions of examples</li>
                    <li>Transformers use attention to understand relationships between words</li>
                    <li>PyTorch and TensorFlow are frameworks for building neural networks</li>
                    <li>You can use pre-trained models instead of building from scratch</li>
                </ul>
            </div>

            <p>Congratulations! You now understand how modern AI actually works. This is complex stuff, and you've grasped it!</p>

            <p>Ready to learn about running AI models locally? Let's continue with <a href="#chapter-25">Chapter 25: Local LLMs</a>!</p>
        </section>
"""

# Read current file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace Chapter 24
import re
pattern = r'<section id="chapter-24".*?</section>'
content = re.sub(pattern, comprehensive_chapter_24, content, flags=re.DOTALL)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Enhanced Chapter 24 with comprehensive Transformers/Layers content!")
