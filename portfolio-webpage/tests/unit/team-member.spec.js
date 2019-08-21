import TeamMember from '../../src/components/sub-layout/team-member.vue';
import { mount } from '@vue/test-utils';


describe('team-member', () => {
  it('should have a prop called member and be an object', () => {
    const componentProps = Object.keys(TeamMember.props);

    expect(componentProps.find(prop => prop === 'member')).toEqual('member');
    expect(typeof TeamMember.props['member']).toBe('object');
  });
});