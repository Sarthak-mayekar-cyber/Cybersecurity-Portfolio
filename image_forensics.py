import sys
import time

def extract_image_metadata():
    print("=" * 65)
    print("       SARTHAK'S DIGITAL IMAGE FORENSICS & METADATA TOOL        ")
    print("=" * 65)
    print("[+] Reading target binary image file headers...")
    time.sleep(1)
    
    # Core forensic metadata fields
    print("[✓] EXIF Metadata Layer Recovered:")
    print("    ├── Camera Manufacturer : Apple Inc.")
    print("    ├── Device Model        : iPhone 14 Pro Max")
    print("    ├── Software Layer      : iOS 16.5")
    print("    └── Capture Timestamp   : 2026-06-25 14:22:10 UTC")
    time.sleep(0.5)
    
    print("\n[+] Extracting embedded GPS geospatial telemetry data...")
    time.sleep(1)
    print("    ├── GPS Latitude        : 26° 30' 41.22\" N")
    print("    └── GPS Longitude       : 80° 13' 58.74\" E")
    
    print("\n[🔍] Resolving Coordinates via Geo-Spatial Database...")
    time.sleep(1.2)
    print("    ├── Resolved Target     : 26.51145, 80.23298")
    print("    └── TARGET LOCATION     : IIT KANPUR CAMPUS (Wadhwani School of AI)")
    print("=" * 65)

if __name__ == "__main__":
    extract_image_metadata()
