import { NextResponse } from "next/server"

export async function POST(req: Request) {
  try {
    const { messages } = await req.json()
    const userMessage = messages[messages.length - 1]?.content

    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage }),
    })

    const data = await res.json()
    return NextResponse.json({ message: data.response })
  } catch (error) {
    console.error("Chat error:", error)
    return NextResponse.json({ error: "Failed to reach FastAPI backend." }, { status: 500 })
  }
}
