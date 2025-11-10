"use client"

import { useRef } from "react"

import type React from "react"
import { useState } from "react"
import { Button } from "@/components/ui/button"
import IntroPage from "@/components/intro-page"
import { Input } from "@/components/ui/input"
import { Spinner } from "@/components/ui/spinner"
import ChatMessage from "@/components/chat-message"

export default function Home() {
  const [showChat, setShowChat] = useState(false)
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hi! I'm Contextia, your intelligent AI assistant. How can I help you today?" },
  ])
  const [input, setInput] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim()) return

    const userMessage = { role: "user", content: input }
    setMessages((prev) => [...prev, userMessage])
    setInput("")
    setIsLoading(true)

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: [...messages, userMessage] }),
      })

      const data = await response.json()
      setMessages((prev) => [...prev, { role: "assistant", content: data.message }])
    } catch (error) {
      console.error("Error:", error)
      setMessages((prev) => [...prev, { role: "assistant", content: "Sorry, something went wrong." }])
    } finally {
      setIsLoading(false)
    }
  }

  if (!showChat) {
    return <IntroPage onStartChat={() => setShowChat(true)} />
  }

  return (
    <div className="flex flex-col h-screen bg-gradient-to-br from-background via-background to-secondary">
      {/* Header */}
      <div className="border-b border-border/40 bg-card/50 backdrop-blur-sm">
        <div className="max-w-4xl mx-auto px-6 py-4">
          <h1 className="text-2xl font-bold text-foreground">Contextia</h1>
          <p className="text-sm text-muted-foreground">Your intelligent AI assistant</p>
        </div>
      </div>

      {/* Chat Container */}
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-4xl mx-auto px-6 py-8 space-y-4">
          {messages.map((msg, idx) => (
            <ChatMessage key={idx} role={msg.role as "user" | "assistant"} content={msg.content} />
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="flex items-center gap-2 text-muted-foreground">
                <Spinner className="h-4 w-4" />
                <span className="text-sm">Contextia is thinking...</span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input Area */}
      <div className="border-t border-border/40 bg-card/50 backdrop-blur-sm">
        <div className="max-w-4xl mx-auto px-6 py-6">
          <form onSubmit={handleSubmit} className="flex gap-3">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask Contextia anything..."
              disabled={isLoading}
              className="flex-1"
            />
            <Button type="submit" disabled={isLoading || !input.trim()}>
              {isLoading ? <Spinner className="h-4 w-4" /> : "Send"}
            </Button>
          </form>
        </div>
      </div>

      <footer className="border-t border-border/40 bg-card/50 backdrop-blur-sm">
        <div className="max-w-4xl mx-auto px-6 py-6">
          <div className="flex flex-col md:flex-row items-center justify-between gap-2 text-xs text-muted-foreground">
            <p>
              © 2025 Contextia — An open-source AI assistant by{" "}
              <a
                href="https://www.linkedin.com/in/asmaa-ibrahim1/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-primary hover:underline transition-colors"
              >
                Asmaa Ibrahim
              </a>{" "}
              &{" "}
              <a
                href="https://www.linkedin.com/in/yousef-ali-b38153304/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-primary hover:underline transition-colors"
              >
                Yousef Ali
              </a>
            </p>
            <p>Powered by Cellula Technologies | Part of the Empowering Energy AI Internship Program</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
