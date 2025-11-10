import { Card } from "@/components/ui/card"

interface ChatMessageProps {
  role: "user" | "assistant"
  content: string
}

export default function ChatMessage({ role, content }: ChatMessageProps) {
  const isUser = role === "user"

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <Card
        className={`max-w-md px-4 py-3 ${
          isUser
            ? "bg-primary text-primary-foreground rounded-2xl rounded-tr-none"
            : "bg-secondary text-secondary-foreground rounded-2xl rounded-tl-none"
        }`}
      >
        <p className="text-sm leading-relaxed">{content}</p>
      </Card>
    </div>
  )
}
