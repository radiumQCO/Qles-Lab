if __name__ == "__main__":
    try:
        from qles_lab.app import main
        main()
    except Exception:
        # A packaged import failure must leave readable evidence, even without a console.
        from pathlib import Path
        import sys
        import traceback
        root = Path(sys.executable).parent if getattr(sys,"frozen",False) else Path(__file__).resolve().parent
        directory = root/"data"
        directory.mkdir(parents=True,exist_ok=True)
        (directory/"startup-error.log").write_text(traceback.format_exc(),encoding="utf-8")
        raise
