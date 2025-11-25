"""
MentalChat16K - Evaluation Demo Script
CMPE 255 - Data Mining Assignment

This script demonstrates how to:
1. Load the MentalChat16K dataset from HuggingFace
2. Explore the dataset structure
3. Visualize topic distributions

Requirements:
    pip install datasets pandas matplotlib seaborn
"""

from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def load_mentalchat16k():
    """Load the MentalChat16K dataset from HuggingFace."""
    print("Loading MentalChat16K dataset...")
    dataset = load_dataset("ShenLab/MentalChat16K")
    print(f"Dataset loaded successfully!")
    print(f"Number of samples: {len(dataset['train'])}")
    return dataset

def explore_dataset(dataset):
    """Explore basic statistics of the dataset."""
    train_data = dataset['train']

    print("\n" + "="*50)
    print("DATASET STATISTICS")
    print("="*50)

    # Convert to pandas for easier analysis
    df = pd.DataFrame(train_data)

    print(f"\nTotal samples: {len(df)}")
    print(f"\nColumns: {list(df.columns)}")

    # Sample entry
    print("\n" + "-"*50)
    print("SAMPLE ENTRY")
    print("-"*50)
    sample = train_data[0]
    for key, value in sample.items():
        print(f"\n{key}:")
        if isinstance(value, str) and len(value) > 200:
            print(f"  {value[:200]}...")
        else:
            print(f"  {value}")

    return df

def calculate_text_statistics(df):
    """Calculate input/output length statistics."""
    print("\n" + "="*50)
    print("TEXT LENGTH STATISTICS")
    print("="*50)

    # Assuming 'input' and 'output' columns exist
    if 'input' in df.columns and 'output' in df.columns:
        df['input_words'] = df['input'].apply(lambda x: len(str(x).split()))
        df['output_words'] = df['output'].apply(lambda x: len(str(x).split()))

        print(f"\nInput (Question) Statistics:")
        print(f"  Mean words: {df['input_words'].mean():.2f}")
        print(f"  Median words: {df['input_words'].median():.2f}")
        print(f"  Max words: {df['input_words'].max()}")

        print(f"\nOutput (Response) Statistics:")
        print(f"  Mean words: {df['output_words'].mean():.2f}")
        print(f"  Median words: {df['output_words'].median():.2f}")
        print(f"  Max words: {df['output_words'].max()}")

    return df

def visualize_distributions(df):
    """Create visualizations of the dataset."""
    print("\n" + "="*50)
    print("GENERATING VISUALIZATIONS")
    print("="*50)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Word count distributions
    if 'input_words' in df.columns:
        axes[0].hist(df['input_words'], bins=50, color='steelblue', edgecolor='black', alpha=0.7)
        axes[0].set_title('Distribution of Input (Question) Lengths')
        axes[0].set_xlabel('Number of Words')
        axes[0].set_ylabel('Frequency')
        axes[0].axvline(df['input_words'].mean(), color='red', linestyle='--', label=f'Mean: {df["input_words"].mean():.1f}')
        axes[0].legend()

    if 'output_words' in df.columns:
        axes[1].hist(df['output_words'], bins=50, color='forestgreen', edgecolor='black', alpha=0.7)
        axes[1].set_title('Distribution of Output (Response) Lengths')
        axes[1].set_xlabel('Number of Words')
        axes[1].set_ylabel('Frequency')
        axes[1].axvline(df['output_words'].mean(), color='red', linestyle='--', label=f'Mean: {df["output_words"].mean():.1f}')
        axes[1].legend()

    plt.tight_layout()
    plt.savefig('../images/length_distributions.png', dpi=300, bbox_inches='tight')
    print("Saved: ../images/length_distributions.png")
    plt.show()

def create_dataset_composition_chart():
    """Create a pie chart showing dataset composition."""
    # Data from the paper
    labels = ['Synthetic Data\n(9,775 pairs)', 'Interview Data\n(6,338 pairs)']
    sizes = [9775, 6338]
    colors = ['#3498db', '#2ecc71']
    explode = (0.05, 0)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=90, textprops={'fontsize': 12})
    ax.set_title('MentalChat16K Dataset Composition\n(Total: 16,113 QA Pairs)', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('../images/dataset_composition.png', dpi=300, bbox_inches='tight')
    print("Saved: ../images/dataset_composition.png")
    plt.show()

def create_metrics_visualization():
    """Create a visualization of the 7 evaluation metrics."""
    metrics = [
        'Active Listening',
        'Empathy & Validation',
        'Safety & Trustworthiness',
        'Open-mindedness',
        'Clarity & Encouragement',
        'Boundaries & Ethics',
        'Holistic Approach'
    ]

    # Sample scores (illustrative - replace with actual data if available)
    base_scores = [6.2, 6.5, 6.0, 6.3, 6.4, 6.1, 6.2]
    finetuned_scores = [8.1, 8.3, 7.9, 8.0, 8.2, 7.8, 8.0]

    x = range(len(metrics))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    bars1 = ax.bar([i - width/2 for i in x], base_scores, width, label='Base Model', color='#e74c3c', alpha=0.8)
    bars2 = ax.bar([i + width/2 for i in x], finetuned_scores, width, label='Fine-tuned Model', color='#27ae60', alpha=0.8)

    ax.set_ylabel('Score (1-10)', fontsize=12)
    ax.set_title('Model Performance Across 7 Therapeutic Metrics', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, rotation=45, ha='right', fontsize=10)
    ax.legend()
    ax.set_ylim(0, 10)
    ax.axhline(y=7, color='gray', linestyle='--', alpha=0.5, label='Threshold')

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.savefig('../images/evaluation_metrics.png', dpi=300, bbox_inches='tight')
    print("Saved: ../images/evaluation_metrics.png")
    plt.show()

def main():
    """Main function to run the evaluation demo."""
    print("="*60)
    print("MentalChat16K - Evaluation Demo")
    print("CMPE 255 - Data Mining Assignment")
    print("="*60)

    # Create static visualizations first (don't require dataset)
    print("\nCreating visualizations...")
    create_dataset_composition_chart()
    create_metrics_visualization()

    # Try to load and explore the dataset
    try:
        dataset = load_mentalchat16k()
        df = explore_dataset(dataset)
        df = calculate_text_statistics(df)
        visualize_distributions(df)
    except Exception as e:
        print(f"\nNote: Could not load dataset from HuggingFace: {e}")
        print("The static visualizations have been created successfully.")

    print("\n" + "="*60)
    print("Demo completed!")
    print("="*60)

if __name__ == "__main__":
    main()
