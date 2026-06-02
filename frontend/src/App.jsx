import React from 'react';
import { LayoutDashboard, Newspaper, TrendingUp, AlertTriangle } from 'lucide-react';

export default function App() {
  return (
    <div className="min-h-screen bg-terminalBg text-[#E2E8F0] flex">
      <aside className="w-64 bg-terminalCard border-r border-terminalBorder p-6 flex flex-col justify-between">
        <div>
          <div className="flex items-center gap-3 mb-8">
            <div className="w-8 h-8 rounded-lg bg-bullishGreen flex items-center justify-center font-bold text-black">Ω</div>
            <span className="text-xl font-bold tracking-wider text-white">ALPHA.AI</span>
          </div>
          <nav className="space-y-2">
            <button className="w-full flex items-center gap-3 px-4 py-3 bg-terminalBorder text-bullishGreen rounded-lg font-medium text-sm">
              <LayoutDashboard size={18} /> Terminal Dashboard
            </button>
            <button className="w-full flex items-center gap-3 px-4 py-3 text-[#94A3B8] hover:bg-[#1E293B] hover:text-white rounded-lg font-medium text-sm">
              <Newspaper size={18} /> Sentiment Archives
            </button>
            <button className="w-full flex items-center gap-3 px-4 py-3 text-[#94A3B8] hover:bg-[#1E293B] hover:text-white rounded-lg font-medium text-sm">
              <AlertTriangle size={18} /> Alert Management
            </button>
          </nav>
        </div>
        <div className="border-t border-terminalBorder pt-4 text-xs text-[#64748B]">
          Terminal Status: <span className="text-bullishGreen font-semibold">ONLINE</span>
        </div>
      </aside>

      <main className="flex-1 p-8 flex flex-col overflow-y-auto">
        <header className="flex justify-between items-center mb-8 pb-4 border-b border-terminalBorder">
          <div>
            <h1 className="text-2xl font-bold text-white tracking-tight">Real-Time Market Intelligence</h1>
            <p className="text-sm text-[#64748B]">Alternative NLP Data Pipeline Feed</p>
          </div>
          <div className="bg-terminalCard px-4 py-2 rounded-lg border border-terminalBorder text-xs font-mono text-[#94A3B8]">
            REFRESH RATE: <span className="text-white font-bold">5M INT / PRICE: LIVE</span>
          </div>
        </header>

        <div className="grid grid-cols-1 xl:grid-cols-3 gap-6 flex-1">
          <div className="xl:col-span-1 bg-terminalCard rounded-xl border border-terminalBorder p-6 flex flex-col">
            <h3 className="text-sm font-semibold tracking-wider text-[#94A3B8] uppercase mb-4 flex items-center gap-2">
              <TrendingUp size={16} className="text-bullishGreen" /> Watchlist Price Stream
            </h3>
            <div className="flex-1 flex items-center justify-center border border-dashed border-terminalBorder rounded-lg text-xs text-[#64748B]">
              Module 2: Live Price Components Container
            </div>
          </div>

          <div className="xl:col-span-2 bg-terminalCard rounded-xl border border-terminalBorder p-6 flex flex-col">
            <h3 className="text-sm font-semibold tracking-wider text-[#94A3B8] uppercase mb-4 flex items-center gap-2">
              <Newspaper size={16} className="text-bullishGreen" /> Real-Time Sentiment Ingestion Feed
            </h3>
            <div className="flex-1 flex items-center justify-center border border-dashed border-terminalBorder rounded-lg text-xs text-[#64748B]">
              Module 3: AI Sentiment Scrape Table Container
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}