"use client"

import { Button } from "@/components/ui/button"
import { ArrowRight, Zap, Brain, Lightbulb } from "lucide-react"

interface IntroPageProps {
  onStartChat: () => void
}

export default function IntroPage({ onStartChat }: IntroPageProps) {
  const features = [
    {
      icon: Brain,
      title: "Context Aware",
      description:
        "More than just a chatbot — Contextia understands background, intent, and nuance. It analyzes your message holistically to deliver answers that make sense in context.",
      color: "from-primary/10 to-primary/5",
      iconColor: "text-primary",
    },
    {
      icon: Zap,
      title: "Instant Responses",
      description:
        "Get clear, accurate answers in seconds. Contextia processes your query intelligently and provides fast, relevant replies — no waiting, no confusion.",
      color: "from-accent/10 to-accent/5",
      iconColor: "text-accent",
    },
    {
      icon: Lightbulb,
      title: "Always Learning",
      description:
        "Continuously evolving with the latest AI advancements. Contextia adapts to new data and feedback to improve its accuracy and depth of understanding every day.",
      color: "from-emerald-500/10 to-emerald-500/5",
      iconColor: "text-emerald-500",
    },
  ]

  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-background to-secondary flex flex-col">
      {/* Header */}
      <header className="border-b border-border/40 bg-card/50 backdrop-blur-sm sticky top-0 z-10">
        <div className="max-w-6xl mx-auto px-6 py-4">
          <h1 className="text-3xl font-bold text-foreground">Contextia</h1>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 flex flex-col items-center justify-center px-6 py-12">
        <div className="max-w-6xl w-full space-y-12">
          {/* Hero Section */}
          <div className="text-center space-y-6">
            <h2 className="text-5xl font-bold text-foreground text-balance">Meet Contextia</h2>
            <p className="text-xl text-muted-foreground text-balance max-w-3xl mx-auto">
              An AI system that follows your reasoning, learns from context, and delivers informed, goal-oriented
              responses.
            </p>
          </div>

          {/* Features Grid */}
          <div className="grid md:grid-cols-3 gap-6">
            {features.map((feature, idx) => {
              const Icon = feature.icon
              return (
                <div
                  key={idx}
                  className="group p-8 rounded-xl bg-card border border-border/40 hover:border-primary/40 transition-all duration-300 hover:shadow-lg hover:shadow-primary/10 cursor-pointer space-y-4"
                >
                  {/* Icon Container */}
                  <div
                    className={`w-14 h-14 bg-gradient-to-br ${feature.color} rounded-lg flex items-center justify-center group-hover:scale-110 transition-transform`}
                  >
                    <Icon className={`w-7 h-7 ${feature.iconColor}`} />
                  </div>

                  {/* Content */}
                  <div className="space-y-2">
                    <h3 className="font-semibold text-lg text-foreground group-hover:text-primary transition-colors">
                      {feature.title}
                    </h3>
                    <p className="text-sm text-muted-foreground leading-relaxed">{feature.description}</p>
                  </div>

                  {/* Arrow Icon - appears on hover */}
                  <div className="pt-2 opacity-0 group-hover:opacity-100 transition-opacity">
                    <ArrowRight className="w-4 h-4 text-primary" />
                  </div>
                </div>
              )
            })}
          </div>

          {/* CTA Section */}
          <div className="flex flex-col items-center gap-6 pt-8">
            <Button onClick={onStartChat} size="lg" className="gap-2 px-8 py-6 text-base">
              Start Chatting with Contextia
              <ArrowRight className="w-4 h-4" />
            </Button>
            <p className="text-sm text-muted-foreground">
              Powered by advanced AI. Your conversations are private and secure.
            </p>
          </div>
        </div>
      </main>

      {/* Professional Footer */}
      <footer className="border-t border-border/40 bg-card/50 backdrop-blur-sm">
        <div className="max-w-6xl mx-auto px-6 py-8">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <p className="text-sm text-muted-foreground text-center md:text-left">
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
            <p className="text-sm text-muted-foreground text-center md:text-right">
              Powered by Cellula Technologies | Part of the Empowering Energy AI Internship Program
            </p>
          </div>
        </div>
      </footer>
    </div>
  )
}
