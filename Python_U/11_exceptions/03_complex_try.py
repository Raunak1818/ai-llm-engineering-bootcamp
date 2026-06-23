def serve_chai(flavor):

    try:
        print(f"preparing {flavor} chai.....")
        if flavor == "unknown":
            raise ValueError("We do not know the flavor")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")


serve_chai("Masala")
serve_chai("unknown")