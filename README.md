# Tawasol Symbols – 3rd Release Powered by AI

A full-stack web application that enables users to generate culturally localized pictograms following the Tawasol Symbols style using OpenAI's GPT-4o model with DALL·E image generation.

## Features

- Responsive UI with bilingual support (English/Arabic)
- Prompt transformation to enforce Tawasol Symbols style
- OpenAI integration for image generation
- Error handling and user feedback

## Project Structure

- `/backend`: FastAPI backend with OpenAI integration
- `/frontend`: React frontend with Tailwind CSS and shadcn/ui

## Setup Instructions

### Backend

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Install dependencies:
   ```
   poetry install
   ```

3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Start the backend server:
   ```
   poetry run fastapi dev app/main.py
   ```

### Frontend

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Create a `.env` file with the backend URL:
   ```
   VITE_API_URL=http://localhost:8000
   ```

4. Start the frontend development server:
   ```
   npm run dev
   ```

5. Open your browser and navigate to `http://localhost:5173`

## Usage

1. Enter a concept in the input field (e.g., "I want to eat")
2. Select the language for the caption (English or Arabic)
3. Click "Generate Image" to create a Tawasol Symbols style pictogram
