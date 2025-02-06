import React, { useState } from 'react';
import { Send, Paperclip, Mic } from 'lucide-react';
import { sendMessage } from '../api/endpoints';

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  conversationId: string;
}

export function ChatInput({ onSendMessage, conversationId }: ChatInputProps) {
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim() && !isLoading) {
      try {
        setIsLoading(true);
        const response = await sendMessage(message, conversationId);
        if (response.success) {
          onSendMessage(message);
          setMessage('');
        } else {
          console.error('Failed to send message:', response.error);
        }
      } catch (error) {
        console.error('Error sending message:', error);
      } finally {
        setIsLoading(false);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="border-t border-gray-200 dark:border-gray-700 p-4">
      <div className="flex items-center gap-2">
        <button
          type="button"
          className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800"
        >
          <Paperclip className="w-5 h-5 text-gray-500 dark:text-gray-400" />
        </button>
        
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type a message..."
          disabled={isLoading}
          className="flex-1 bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white rounded-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
        />
        
        <button
          type="button"
          className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800"
        >
          <Mic className="w-5 h-5 text-gray-500 dark:text-gray-400" />
        </button>
        
        <button
          type="submit"
          disabled={isLoading || !message.trim()}
          className="p-2 bg-blue-600 rounded-full hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <Send className="w-5 h-5 text-white" />
        </button>
      </div>
    </form>
  );
}