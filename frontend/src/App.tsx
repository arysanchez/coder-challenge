import React, { useState } from 'react';
import { Sidebar } from './components/Sidebar';
import { ChatMessage } from './components/ChatMessage';
import { ChatInput } from './components/ChatInput';
import { Activity } from 'lucide-react';
import type { Message, Conversation } from './types';
import { toggleFavorite } from './api/endpoints';

const initialConversations: Conversation[] = [
  {
    id: '1',
    title: 'Project Discussion',
    lastMessage: 'Let\'s review the requirements',
    timestamp: new Date(),
    isFavorite: false,
  },
  {
    id: '2',
    title: 'Technical Support',
    lastMessage: 'How can I help you today?',
    timestamp: new Date(),
    isFavorite: false,
  },
];

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [conversations, setConversations] = useState<Conversation[]>(initialConversations);
  const [currentConversationId, setCurrentConversationId] = useState<string | null>(null);
  const [showFavoritesOnly, setShowFavoritesOnly] = useState(false);

  const handleSendMessage = (content: string) => {
    if (!currentConversationId) return;

    const newMessage: Message = {
      id: Date.now().toString(),
      content,
      sender: 'user',
      timestamp: new Date(),
    };
    
    setMessages([...messages, newMessage]);
    
    // Update last message in conversation
    setConversations(prevConversations =>
      prevConversations.map(conv =>
        conv.id === currentConversationId
          ? { ...conv, lastMessage: content, timestamp: new Date() }
          : conv
      )
    );
  };

  const handleNewChat = (conversation: Conversation) => {
    setConversations(prev => [conversation, ...prev]);
    setCurrentConversationId(conversation.id);
    setMessages([]);
  };

  const handleToggleFavorite = async (conversationId: string) => {
    const conversation = conversations.find(c => c.id === conversationId);
    if (!conversation) return;

    const newIsFavorite = !conversation.isFavorite;
    
    try {
      const response = await toggleFavorite(conversationId, newIsFavorite);
      if (response.success) {
        setConversations(prevConversations =>
          prevConversations.map(conv =>
            conv.id === conversationId
              ? { ...conv, isFavorite: newIsFavorite }
              : conv
          )
        );
      }
    } catch (error) {
      console.error('Error toggling favorite:', error);
    }
  };

  const handleSelectConversation = (conversationId: string) => {
    setCurrentConversationId(conversationId);
    setMessages([]); // Clear messages when switching conversations
  };

  const filteredConversations = showFavoritesOnly
    ? conversations.filter(conv => conv.isFavorite)
    : conversations;

  return (
    <div className={isDarkMode ? 'dark' : ''}>
      <div className="flex h-screen bg-gray-50 dark:bg-gray-900">
        <Sidebar
          conversations={filteredConversations}
          isDarkMode={isDarkMode}
          onToggleDarkMode={() => setIsDarkMode(!isDarkMode)}
          onNewChat={handleNewChat}
          onToggleFavorite={handleToggleFavorite}
          showFavoritesOnly={showFavoritesOnly}
          onToggleShowFavorites={() => setShowFavoritesOnly(!showFavoritesOnly)}
        />
        
        <main className="flex-1 flex flex-col">
          <div className="p-4 border-b border-gray-200 dark:border-gray-700 flex items-center justify-between">
            <h1 className="text-xl font-semibold text-gray-800 dark:text-white">Chat</h1>
            <div className="flex items-center gap-2">
              <Activity className="w-4 h-4 text-green-500 animate-pulse" />
              <span className="text-sm text-gray-500 dark:text-gray-400">Online</span>
            </div>
          </div>
          
          <div className="flex-1 overflow-y-auto p-4">
            {messages.map((message) => (
              <ChatMessage key={message.id} message={message} />
            ))}
          </div>
          
          <ChatInput 
            onSendMessage={handleSendMessage} 
            conversationId={currentConversationId || ''}
          />
        </main>
      </div>
    </div>
  );
}

export default App;