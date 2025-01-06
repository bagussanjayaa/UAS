class Process:
    @staticmethod
    def validate_nilai(nilai):
        try:
            nilai = float(nilai)
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus antara 0 dan 100.")
            return nilai
        except ValueError as e: print(f"Input tidak valid: {e}")
        return None
    