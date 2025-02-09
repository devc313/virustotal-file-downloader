# virustotal api ile dosya indirme by ecvd


import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import vt
import os
from pathlib import Path


console = Console()
app = typer.Typer()

# vt api key
API_KEY = "YOUR_API_KEY"

@app.command()
def download_file(
    hash: str = typer.Argument(..., help="İndirilecek dosyanın hash değeri"),
    output_dir: str = typer.Option(
        "downloads",
        "--output-dir", "-o",
        help="Dosyanın indirileceği dizin"
    )
):
    """
    VirusTotal'dan belirtilen hash değerine sahip dosyayı indir.
    """
    try:
        # gotumuzemi sokacaz dosyalari dizin ac
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            # vt clienti ac kardesim
            progress.add_task(description="VirusTotal'a bağlanılıyor...", total=None)
            client = vt.Client(API_KEY)

            try:
                # dosya bilgilerini al
                file = client.get_object(f"/files/{hash}")
                
                # ne indirecez bi bakak reis
                file_name = getattr(file, "meaningful_name", hash)
                output_file = output_path / file_name

                progress.add_task(description=f"[cyan]{file_name} indiriliyor...[/]", total=None)
                
                # al kac dosyayi bakim
                with open(output_file, "wb") as f:
                    data = client.get_object(f"/files/{hash}/download")
                    f.write(data.read())

                console.print(f"[green]✓[/] Dosya başarıyla indirildi: {output_file}")

            finally:
                client.close()

    except vt.APIError as e:
        console.print(f"[red]Hata:[/] VirusTotal API hatası: {str(e)}")
    except Exception as e:
        console.print(f"[red]Hata:[/] Beklenmeyen bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    app() 