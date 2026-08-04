export default function DepartmentBadge({ dept, size = 'md' }) {
  if (!dept) return null;
  return (
    <span
      className={`dept-badge dept-badge--${size}`}
      style={{ '--dept-color': dept.color, '--dept-bg': dept.bg }}
      title={dept.label}
    >
      {dept.short}
    </span>
  );
}
