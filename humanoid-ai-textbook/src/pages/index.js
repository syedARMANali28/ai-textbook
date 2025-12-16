import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './NewHomepage.module.css';
import RagChat from '../components/RagChat.jsx';
import UrduTranslate from '../components/UrduTranslate.jsx';

function HomepageHeader() {
  return (
    <header className={styles.heroBanner}>
      <div className={styles.container}>
        <h1 className={styles.heroTitle}>AI-Native Humanoid Robotics</h1>
        <p className={styles.heroSubtitle}>
          Learn Physical AI, Humanoid Robotics, and Voice-to-Action
        </p>
        <div className={styles.buttons}>
          <Link className={styles.button} to="/docs/ros2-module-spec/">
            ROS 2 Module
          </Link>
          <Link className={styles.button} to="/docs/vla-module/">
            VLA Module
          </Link>
          <Link className={styles.button} to="/docs/digital-twin-module/">
            Digital Twin Module
          </Link>
          <Link className={styles.button} to="/docs/nvidia-isaac-module/">
            NVIDIA Isaac Module
          </Link>
        </div>
      </div>
    </header>
  );
}

function ComponentsSection() {
  return (
    <div className={styles.componentsContainer}>
      <div className={styles.componentWrapper}>
        <h2>RAG Chat</h2>
        <RagChat />
      </div>
      <div className={styles.componentWrapper}>
        <h2>Urdu Translation</h2>
        <UrduTranslate />
      </div>
    </div>
  );
}

export default function Home() {
  return (
    <Layout
      title="AI-Native Humanoid Robotics"
      description="Learn Physical AI, Humanoid Robotics, and Voice-to-Action"
    >
      <HomepageHeader />
      <main>
        <ComponentsSection />
      </main>
    </Layout>
  );
}