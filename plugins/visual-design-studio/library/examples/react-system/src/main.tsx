// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { SpecimenApp } from './specimen/App';
import './styles/index.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <SpecimenApp />
  </StrictMode>,
);
