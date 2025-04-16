import { useState } from 'react';
import { Loader2, Image as ImageIcon } from 'lucide-react';
import { generateImage } from '../services/api';
import { ImageGenerationResponse } from '../types';

import { Button } from './ui/button';
import { Input } from './ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from './ui/select';
import { Card, CardContent } from './ui/card';
import { Alert, AlertDescription } from './ui/alert';

interface ImageGeneratorProps {
  direction: 'ltr' | 'rtl';
}

export function ImageGenerator({ direction }: ImageGeneratorProps) {
  const [concept, setConcept] = useState('');
  const [language, setLanguage] = useState('english');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ImageGenerationResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!concept.trim()) {
      setError('Please enter a concept');
      return;
    }
    
    setLoading(true);
    setError(null);
    
    try {
      const response = await generateImage({
        concept: concept.trim(),
        language,
      });
      
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to generate image');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`flex flex-col gap-6 w-full max-w-md mx-auto ${direction === 'rtl' ? 'text-right' : 'text-left'}`} dir={direction}>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <div className="space-y-2">
          <label htmlFor="concept" className="text-sm font-medium">
            {direction === 'rtl' ? 'أدخل المفهوم' : 'Enter Concept'}
          </label>
          <Input
            id="concept"
            placeholder={direction === 'rtl' ? 'مثال: أريد أن آكل' : 'Example: I want to eat'}
            value={concept}
            onChange={(e) => setConcept(e.target.value)}
            disabled={loading}
            className="w-full"
          />
        </div>
        
        <div className="space-y-2">
          <label htmlFor="language" className="text-sm font-medium">
            {direction === 'rtl' ? 'اختر اللغة' : 'Select Language'}
          </label>
          <Select
            value={language}
            onValueChange={setLanguage}
            disabled={loading}
          >
            <SelectTrigger id="language" className="w-full">
              <SelectValue placeholder={direction === 'rtl' ? 'اختر اللغة' : 'Select language'} />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="english">English</SelectItem>
              <SelectItem value="arabic">Arabic (العربية)</SelectItem>
            </SelectContent>
          </Select>
        </div>
        
        <Button type="submit" disabled={loading} className="w-full mt-2">
          {loading ? (
            <>
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
              {direction === 'rtl' ? 'جاري التوليد...' : 'Generating...'}
            </>
          ) : (
            <>
              <ImageIcon className="mr-2 h-4 w-4" />
              {direction === 'rtl' ? 'توليد الصورة' : 'Generate Image'}
            </>
          )}
        </Button>
      </form>
      
      {error && (
        <Alert variant="destructive">
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}
      
      {result && !loading && (
        <Card>
          <CardContent className="p-4 flex flex-col items-center">
            <div className="relative w-full aspect-square mb-4 bg-gray-100 rounded-md overflow-hidden">
              <img 
                src={result.image_url} 
                alt={concept}
                className="w-full h-full object-contain"
              />
            </div>
            <p className="text-sm text-center text-gray-700">
              {concept}
            </p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
