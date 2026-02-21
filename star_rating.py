def create_star_rating(rating: float) -> str:
    """
    Create a star rating visualization with filled stars based on input rating.
    Uses inline SVG for reliable cross-platform rendering.

    Parameters
    ----------
    rating : float
        A number between 1 and 5 (inclusive). Supports decimal values for partial stars.

    Returns
    -------
    str
        HTML string with star rating visualization
    """
    # Validate and clamp input between 1 and 5
    rating = max(1.0, min(5.0, rating))

    star_path = "M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"

    def filled_star():
        return f'<svg width="16" height="16" viewBox="0 0 24 24" fill="gold" style="display:inline-block;vertical-align:middle;"><path d="{star_path}"/></svg>'

    def empty_star():
        return f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="lightgray" stroke-width="2" style="display:inline-block;vertical-align:middle;"><path d="{star_path}"/></svg>'

    def half_star():
        return f'''<svg width="16" height="16" viewBox="0 0 24 24" style="display:inline-block;vertical-align:middle;">
            <defs><clipPath id="half"><rect x="0" y="0" width="12" height="24"/></clipPath></defs>
            <path d="{star_path}" fill="none" stroke="lightgray" stroke-width="2"/>
            <path d="{star_path}" fill="gold" clip-path="url(#half)"/>
        </svg>'''

    # Calculate number of full, half and empty stars
    full_stars = int(rating)
    has_half_star = rating % 1 >= 0.5
    empty_stars = 5 - full_stars - (1 if has_half_star else 0)

    # Create star HTML elements
    stars_html = '<span style="white-space:nowrap;">'

    for _ in range(full_stars):
        stars_html += filled_star()

    if has_half_star:
        stars_html += half_star()

    for _ in range(empty_stars):
        stars_html += empty_star()

    stars_html += '</span>'

    return stars_html