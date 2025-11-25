import requests
from typing import Optional
from app.config import get_settings

settings = get_settings()

class ImageService:
    def __init__(self):
        self.pexels_api_key = settings.pexels_api_key if hasattr(settings, 'pexels_api_key') else None
        self.base_url = "https://api.pexels.com/v1/search"
    
    def search_image(self, query: str, orientation: str = "landscape") -> Optional[str]:
        """
        Search for a relevant image using Pexels API
        Returns image URL or None if not found/API key missing
        """
        if not self.pexels_api_key:
            return None
        
        try:
            headers = {
                "Authorization": self.pexels_api_key
            }
            params = {
                "query": query,
                "per_page": 1,
                "orientation": orientation,
                "size": "medium"
            }
            
            response = requests.get(self.base_url, headers=headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("photos") and len(data["photos"]) > 0:
                    # Return the medium-sized landscape image URL
                    return data["photos"][0]["src"]["large"]
            
            return None
        except Exception as e:
            print(f"Error fetching image for '{query}': {str(e)}")
            return None
    
    def download_image(self, image_url: str) -> Optional[bytes]:
        """
        Download image bytes from URL
        Returns image bytes or None if failed
        """
        try:
            response = requests.get(image_url, timeout=15)
            if response.status_code == 200:
                return response.content
            return None
        except Exception as e:
            print(f"Error downloading image from {image_url}: {str(e)}")
            return None

image_service = ImageService()
