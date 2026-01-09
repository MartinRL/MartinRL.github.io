# Image Descriptions for LLM Concepts Slides

## 1. tokens-visualization.png
**Concept**: Tokenization
**Description**: A visual showing text being broken down into tokens/chunks
**Suggested image**:
- Text example like "Hello world!" being split into ["Hello", " world", "!"]
- Color-coded boxes showing each token with its numerical ID
- Similar to OpenAI's tokenizer visualization tool

## 2. transformer-architecture.png
**Concept**: Transformer Architecture
**Description**: Simplified transformer architecture diagram
**Suggested image**:
- The classic "Attention is All You Need" architecture diagram simplified
- Show encoder-decoder structure with attention mechanisms
- Highlight the self-attention connections between words

## 3. parameters-network.png
**Concept**: Neural Network Parameters
**Description**: Visualization of neural network weights/parameters
**Suggested image**:
- Neural network with nodes and weighted connections
- Show connections as lines with varying thickness representing weight values
- Could use a heat map showing parameter density

## 4. probability-distribution.png
**Concept**: Probability Distribution
**Description**: Graph showing word probability distribution
**Suggested image**:
- Bar chart or curve showing probability values for next word predictions
- Example: "The capital of France is..." with probabilities for "Paris" (0.95), "Lyon" (0.02), etc.
- Softmax distribution visualization

## 5. context-window.png
**Concept**: Context Window/Memory
**Description**: Visual metaphor for context window limitations
**Suggested image**:
- Sliding window over text showing what's "in view" vs what's forgotten
- Memory buffer visualization with overflow
- Timeline showing conversation history with visible vs forgotten sections

## 6. temperature-effects.png
**Concept**: Temperature Parameter Effects
**Description**: Comparison of outputs at different temperature settings
**Suggested image**:
- Side-by-side text samples at temp=0, 0.7, and 2.0
- Probability distribution curves getting flatter as temperature increases
- Creative vs deterministic output examples

## Resources for Images:
- Wolfram's book has excellent tokenization diagrams
- The Illustrated Transformer blog has great architecture visuals
- Papers With Code has parameter visualization examples
- OpenAI's playground shows temperature effects visually