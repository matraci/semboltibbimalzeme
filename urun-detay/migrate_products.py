import os
from bs4 import BeautifulSoup
import re

# Target Template (based on user request)
TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{title}</title>

    <meta name="description" content="{meta_description}">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">

    <style>
        body{{
            font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto;
            background:#ffffff;
            color:#111;
        }}

        .section{{
            padding:100px 20px;
        }}

        .hero{{
            padding:120px 20px;
        }}

        .hero h1{{
            font-size:48px;
            font-weight:700;
            letter-spacing:-1px;
        }}

        .hero p{{
            font-size:20px;
            color:#555;
        }}

        .btn-premium{{
            padding:10px 22px;
            border-radius:50px;
            font-weight:500;
        }}

        .light-section{{
            background:#f5f5f7;
        }}

        .feature-box{{
            text-align:center;
            padding:40px 20px;
        }}

        .feature-box i{{
            font-size:32px;
            margin-bottom:20px;
        }}

        .table thead th{{
            font-weight:600;
            font-size:14px;
            letter-spacing:0.5px;
            color:#666;
            border-bottom:2px solid #eee;
        }}

        .table tbody tr{{
            transition:0.3s;
        }}

        .table tbody tr:hover{{
            background:#f5f5f7;
        }}

        .table td{{
            padding:18px 10px;
            vertical-align:middle;
        }}

        ul{{
            padding-left:18px;
        }}
        .page-header{{
            padding:60px 0;
            background:#f5f5f7;
        }}

        .breadcrumb{{
            background:transparent;
            padding:0;
            margin-bottom:0;
        }}
        .header-area {{
            background: #fff;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            position: sticky;
            top: 0;
            z-index: 1000;
        }}
        .navbar-brand img {{
            height: 60px;
        }}
        .nav-link {{
            font-weight: 500;
            color: #333;
            margin-left: 15px;
        }}
        .nav-link:hover, .nav-link.active {{
            color: #d63384; 
        }}
        .hamburger span {{
            display: block;
            width: 25px;
            height: 3px;
            margin: 5px auto;
            background-color: #333;
            transition: 0.3s;
        }}
    </style>
</head>

<body>

    <!-- NAVBAR -->
    <header class="header-area" id="header">
        <div class="container">
            <nav class="navbar navbar-expand-lg">
                <a class="navbar-brand logo" href="../index.html">
                    <img src="../upload/396e08540e.png" alt="SembolTibbi" style="height: 60px;">
                </a>
                <button class="navbar-toggler hamburger" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span></span><span></span><span></span>
                </button>
                <div class="collapse navbar-collapse main-menu" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="../index.html">Ana Sayfa</a></li>
                        <li class="nav-item"><a class="nav-link" href="../hakkimizda.html">Hakkımızda</a></li>
                        <li class="nav-item"><a class="nav-link active" href="../urun/index.html">Ürünler</a></li>
                        <li class="nav-item"><a class="nav-link" href="../bakimlar.html">Bakımlar</a></li>
                        <li class="nav-item"><a class="nav-link" href="../iletisim.html">İletişim</a></li>
                    </ul>
                </div>
            </nav>
        </div>
    </header>

    <!-- PAGE HEADER -->
    <section class="page-header">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-8">
                    <h1 class="fade-in visible">{product_name}</h1>
                    <nav aria-label="breadcrumb" class="fade-in visible">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item"><a href="../index.html">Ana Sayfa</a></li>
                            <li class="breadcrumb-item"><a href="../urun/index.html">Ürünler</a></li>
                            <li class="breadcrumb-item active" aria-current="page">{product_name}</li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
    </section>

    <!-- HERO -->
    <section class="hero">
        <div class="container">
            <div class="row align-items-center">

                <div class="col-lg-6 mb-5">
                    <!-- Title moved to page-header -->

                    <div class="mt-4 hero-description">
                        {short_description}
                    </div>

                    <div class="mt-4">
                        <a href="#iletisim" class="btn btn-dark btn-premium me-3">Bilgi Al</a>
                        <a href="#sgk" class="btn btn-outline-dark btn-premium">SGK Bilgisi</a>
                    </div>

                </div>

                <div class="col-lg-6 text-center">
                    <img src="{image_src}" class="img-fluid rounded-4 shadow" alt="{product_name}">
                </div>

            </div>
        </div>
    </section>

    <!-- DETAYLI AÇIKLAMA -->
    <section class="section light-section" id="aciklama">
        <div class="container">


            <div class="product-content">
                {detailed_description}
            </div>

        </div>
    </section>

    <!-- ÖZELLİKLER (Generic/Placeholder) -->
    <section class="section">
        <div class="container text-center">

            <h2 class="mb-5">Teknoloji ve Avantajlar</h2>

            <div class="row">

                <div class="col-md-4 feature-box">
                    <i class="fa-solid fa-shield-halved"></i>
                    <h3 class="h5">Güvenli Kullanım</h3>
                    <p>Maksimum güvenlik ve konfor sağlayan yapı.</p>
                </div>

                <div class="col-md-4 feature-box">
                    <i class="fa-solid fa-wind"></i>
                    <h3 class="h5">Konforlu Tasarım</h3>
                    <p>Günlük yaşamda rahatlık sunan ergonomik tasarım.</p>
                </div>

                <div class="col-md-4 feature-box">
                    <i class="fa-solid fa-check"></i>
                    <h3 class="h5">Kolay Uygulama</h3>
                    <p>Pratik ve hızlı kullanım imkanı.</p>
                </div>

            </div>
        </div>
    </section>

    <!-- TEKNİK DETAY (Optional/Placeholder) -->
    <!--
    <section class="section light-section">
        <div class="container">
            <h2 class="text-center mb-5">Teknik Özellikler</h2>
            <ul>
                <li>Özellik 1</li>
                <li>Özellik 2</li>
            </ul>
        </div>
    </section>
    -->

    <!-- ÜRÜN SEÇENEKLERİ TABLO -->
    <section class="section">
        <div class="container">

            <h2 class="text-center mb-5">Ürün Seçenekleri ve Ölçüler</h2>

            <div class="table-responsive">
                <table class="table align-middle text-center">

                    <thead>
                        <tr>
                            <th>Ürün Kodu</th>
                            <th>Tip (Açıklama)</th>
                            <th>Kutu İçeriği</th>
                            <th>Ölçü</th>
                            <th>Renk</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        {table_rows}
                    </tbody>
                </table>
            </div>

        </div>
    </section>

    <!-- SGK -->
    <section id="sgk" class="section light-section text-center">
        <div class="container">

            <h2>SGK Geri Ödeme Süreci</h2>

            <p class="mt-4">
                Bu ürün Sosyal Güvenlik Kurumu geri ödeme kapsamındadır. 
                Reçete ve evrak sürecinde uzman ekibimiz hastalarımıza destek sağlamaktadır.
            </p>

            <a href="#iletisim" class="btn btn-dark btn-premium mt-4">
                SGK Süreci Hakkında Bilgi Al
            </a>

        </div>
    </section>

    <!-- İLETİŞİM / FOOTER PARTIAL (Simplified for single page, pointing to main site) -->
    <section id="iletisim" class="section text-center">
        <div class="container">
            <h2>İletişim</h2>
            <p>Detaylı bilgi ve sipariş için bize ulaşın.</p>
            <a href="../iletisim.html" class="btn btn-primary btn-premium">İletişim Sayfasına Git</a>
        </div>
    </section>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
"""

def load_product_images():
    """
    Parses index.html to create a mapping of product filenames to their image sources.
    Returns: dict {filename: image_src}
    """
    images_map = {}
    try:
        # Assuming index.html is in the same directory or parent
        # The script is in urun-detay, index.html is in urun-detay
        with open("index.html", "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            
        articles = soup.find_all("article", class_="postbox")
        for article in articles:
            # Find the link to the product detail
            link = article.find("a", href=True)
            if link:
                href = link['href']
                # href might be "../urun-detay/filename.html" or similar
                filename = os.path.basename(href)
                
                # Find the image
                img = article.find("img")
                if img and img.get("src"):
                    images_map[filename] = img["src"]
                    
        print(f"Loaded {len(images_map)} image mappings from index.html")
        return images_map
    except Exception as e:
        print(f"Error loading image mappings: {e}")
        return {}

def extract_data(filepath, images_map=None):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    data = {}
    filename = os.path.basename(filepath)
    
    # 1. Product Name (H1)
    # Check if we are in a migrated file (page-header exists)
    page_header_h1 = soup.select_one('.page-header h1')
    hero_h1 = soup.select_one('.hero h1')
    
    if page_header_h1:
        data['product_name'] = page_header_h1.get_text(strip=True)
    elif hero_h1:
        data['product_name'] = hero_h1.get_text(strip=True)
    else:
        h1 = soup.find('h1')
        data['product_name'] = h1.get_text(strip=True) if h1 else "Ürün Adı"

    # 2. Title and Meta Description
    data['title'] = soup.title.string.strip() if soup.title else data['product_name']
    
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    data['meta_description'] = meta_desc['content'] if meta_desc else ""

    # 3. Image
    # PRIORITY: Use the map from index.html if available
    if images_map and filename in images_map:
        data['image_src'] = images_map[filename]
    else:
        # Try to find existing image in the file
        # Check for the new format first
        hero_img = soup.select_one('.col-lg-6 img')
        
        # Check for old format (swiper)
        swiper_img = soup.select_one('.swiper-slide img')
        
        if hero_img and "placeholder" not in hero_img.get('src', ''):
             data['image_src'] = hero_img['src']
        elif swiper_img:
            data['image_src'] = swiper_img['src']
        else:
            data['image_src'] = "../upload/placeholder.png"

    # 4. Description
    aciklama_div = soup.find(id='aciklama')
    if aciklama_div:
        # Clean up H3/H4 tags to avoid duplication if re-running
        for header in aciklama_div.find_all(['h3', 'h4']):
             if "Ürün Tanı" in header.get_text() or "Nedir?" in header.get_text():
                header.decompose()
        
        # Also remove the wrapper div if it was added by previous migration?
        # product-content div inside aciklama? 
        # Existing: <section id="aciklama">... <div class="product-content"> ... </div>
        # We just want the content INSIDE product-content if it exists
        prod_content = aciklama_div.find(class_='product-content')
        if prod_content:
             data['detailed_description'] = str(prod_content.encode_contents().decode('utf-8'))
        else:
             data['detailed_description'] = str(aciklama_div.encode_contents().decode('utf-8'))
        
        # Try to get short text
        first_p = aciklama_div.find('p')
        if first_p:
            data['short_description'] = first_p.get_text(strip=True)[:250] + "..."
        else:
            data['short_description'] = data['product_name'] + " hakkında detaylı bilgi."
    else:
        data['detailed_description'] = "<p>Ürün detayları hazırlanıyor.</p>"
        data['short_description'] = ""

    # 5. Table Rows
    table = soup.find('table')
    rows_html = ""
    if table:
        tbody = table.find('tbody')
        if tbody:
            for tr in tbody.find_all('tr'):
                cols = tr.find_all('td')
                # Start index depends on whether it is old or new table
                # New table has 6 cols (Code, Desc, Content, Size, Color, Button)
                # Old table has similar but maybe different order?
                # If re-running, the table is ALREADY the new table!
                # We need to extract data from NEW table and re-generate row to avoid duplicating buttons or weirdness
                
                # Check directly if it's already migrated row
                if tr.find('a', class_='btn-premium'):
                    # Already migrated row. Just keep it? Or extract?
                    # If we blindly keep it, we might wrap it again? No, we extract keys.
                    # Let's try to extract text from cols.
                    # New table: Code(0), Desc(1), Content(2), Size(3), Color(4), Button(5)
                    # But wait, logic below assumes old table format: cols[1] -> Code.
                    # Old table: [Empty/Checkbox], Code, Desc, Content, Size, Color
                    
                    # If we are re-processing a migrated file, 'table' is generic <table>?
                    # In migrated file: <table class="table ..."> with <thead>...
                    # Cols: Code, Type, Content, Size, Color, [Button]
                    # So index 0 is Code.
                    
                    if len(cols) >= 5:
                         # Identify if it is New or Old
                         first_col_text = cols[0].get_text(strip=True)
                         second_col_text = cols[1].get_text(strip=True)
                         
                         # Old: Col0 is usually empty or checkbox. Col1 is Code.
                         # New: Col0 is Code.
                         
                         is_new_table = False
                         if tr.find('a', class_='btn-premium'):
                             is_new_table = True
                        
                         if is_new_table:
                             code = cols[0].get_text(strip=True)
                             desc = cols[1].get_text(strip=True)
                             content = cols[2].get_text(strip=True)
                             size = cols[3].get_text(strip=True)
                             color = cols[4].get_text(strip=True)
                         else:
                             # Old format assumption
                             code = cols[1].get_text(strip=True)
                             desc = cols[2].get_text(strip=True)
                             content = cols[3].get_text(strip=True)
                             size = cols[4].get_text(strip=True)
                             color = cols[5].get_text(strip=True) if len(cols) > 5 else "-"
                
                         row_html = f"""
                         <tr>
                             <td><strong>{code}</strong></td>
                             <td>{desc}</td>
                             <td>{content}</td>
                             <td>{size}</td>
                             <td>{color}</td>
                             <td><a href="#iletisim" class="btn btn-sm btn-dark btn-premium">Bilgi Al</a></td>
                         </tr>
                         """
                         rows_html += row_html
                elif len(cols) >= 5:
                     # Fallback to old format logic
                    code = cols[1].get_text(strip=True)
                    desc = cols[2].get_text(strip=True)
                    content = cols[3].get_text(strip=True)
                    size = cols[4].get_text(strip=True)
                    color = cols[5].get_text(strip=True) if len(cols) > 5 else "-"
                    
                    if not code and not desc: continue 

                    row_html = f"""
                    <tr>
                        <td><strong>{code}</strong></td>
                        <td>{desc}</td>
                        <td>{content}</td>
                        <td>{size}</td>
                        <td>{color}</td>
                        <td><a href="#iletisim" class="btn btn-sm btn-dark btn-premium">Bilgi Al</a></td>
                    </tr>
                    """
                    rows_html += row_html

    data['table_rows'] = rows_html
    return data

def main():
    directory = "c:/Users/matra/Documents/semboltibbi/semboltibbi_clone/urun-detay"
    
    # Load image mappings
    images_map = load_product_images()

    # Process all HTML files
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "index.html" and "migrated" not in filename:
            filepath = os.path.join(directory, filename)
            print(f"Processing {filename}...")
            
            try:
                data = extract_data(filepath, images_map)
                new_html = TEMPLATE.format(**data)
                
                # Overwrite the original file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                    
                print(f"Updated {filename}")
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
