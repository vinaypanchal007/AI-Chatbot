<script setup>
import '../styles/limitations.css'

const highlights = [
  {
    title: 'Live data',
    text: 'I can work with general knowledge, but I don’t browse the web or pull fresh live information in real time.'
  },
  {
    title: 'No personal memory',
    text: 'I don’t keep long-term memory from previous chats and treat each conversation as fresh.'
  },
  {
    title: 'Safety and boundaries',
    text: 'I avoid disallowed content and I’m not a substitute for professional judgment in medical, legal, or financial matters.'
  }
]
</script>

<template>
  <div class="limitations-panel">
    <header class="hero">
      <div class="eyebrow">AI system overview</div>
      <h2>Important things to know</h2>
      <p>
        I’m useful for brainstorming, summarizing, and explaining ideas, but I do have a few important boundaries.
      </p>
    </header>

    <div class="cards">
      <article v-for="item in highlights" :key="item.title" class="highlight-card">
        <span class="badge">{{ item.title }}</span>
        <p>{{ item.text }}</p>
      </article>
    </div>

    <div class="footer-card">
      <h3>Bottom line</h3>
      <p>
        I can help with general information and writing, but for real-time updates, personal history, or professional advice, it’s best to use dedicated tools or qualified experts.
      </p>
    </div>
  </div>
</template>

