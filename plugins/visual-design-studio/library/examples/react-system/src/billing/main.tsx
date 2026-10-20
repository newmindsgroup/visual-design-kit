// Version-Timestamp: 2026-10-20 02:52:00 UTC
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import '../styles/index.css';
import { BillingRoot } from './BillingApp';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BillingRoot />
  </StrictMode>,
);
