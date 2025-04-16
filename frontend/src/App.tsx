import { useState } from 'react';
import './App.css';
import { ImageGenerator } from './components/ImageGenerator';
import { Button } from './components/ui/button';
import { Globe } from 'lucide-react';

function App() {
  const [direction, setDirection] = useState<'ltr' | 'rtl'>('ltr');
  const [language, setLanguage] = useState<'english' | 'arabic'>('english');

  const toggleLanguage = () => {
    if (language === 'english') {
      setLanguage('arabic');
      setDirection('rtl');
    } else {
      setLanguage('english');
      setDirection('ltr');
    }
  };

  return (
    <div className={`min-h-screen bg-gray-50 ${direction === 'rtl' ? 'font-arabic' : 'font-sans'}`} dir={direction}>
      <header className="bg-white shadow-sm">
        <div className="container mx-auto p-4 flex justify-between items-center">
          <h1 className={`text-2xl font-bold ${direction === 'rtl' ? 'order-2' : 'order-1'}`}>
            {language === 'english' ? 'Tawasol Symbols' : 'رموز تواصل'}
          </h1>
          <Button 
            variant="outline" 
            size="sm" 
            onClick={toggleLanguage}
            className={`${direction === 'rtl' ? 'order-1' : 'order-2'}`}
          >
            <Globe className="h-4 w-4 mr-2" />
            {language === 'english' ? 'العربية' : 'English'}
          </Button>
        </div>
      </header>

      <main className="container mx-auto p-4 py-8">
        <div className="max-w-2xl mx-auto">
          <div className="bg-white rounded-lg shadow-md p-6 mb-6">
            <h2 className="text-xl font-semibold mb-4">
              {language === 'english' 
                ? 'Generate Tawasol Symbols' 
                : 'توليد رموز تواصل'}
            </h2>
            <p className="text-gray-600 mb-6">
              {language === 'english'
                ? 'Enter a concept to generate a culturally localized pictogram in the Tawasol Symbols style.'
                : 'أدخل مفهومًا لتوليد رسم توضيحي محلي ثقافيًا بأسلوب رموز تواصل.'}
            </p>
            <ImageGenerator direction={direction} />
          </div>
        </div>
      </main>

      <footer className="bg-white border-t mt-auto">
        <div className="container mx-auto p-4 text-center text-gray-500 text-sm">
          {language === 'english'
            ? '© 2025 Tawasol Symbols – 3rd Release Powered by AI'
            : '© 2025 رموز تواصل - الإصدار الثالث مدعوم بالذكاء الاصطناعي'}
        </div>
      </footer>
    </div>
  );
}

export default App;
